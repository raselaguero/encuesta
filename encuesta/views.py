from django.shortcuts import render, redirect, get_object_or_404
from .models import Encuesta, Intereses
from .form import EncuestaForm, InteresesForm
from django.http import HttpResponse
from reportlab.platypus import TableStyle, SimpleDocTemplate, Table
from reportlab.lib import colors, pagesizes
from django.views.generic import View

# Create your views here.


def inicio(request):  #todo: ok
    return render(request, 'inicio.html')


def agregar_encuesta(request):  #todo: ok
    form = EncuestaForm()
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            encuesta = form.save()
            pk = encuesta.id
            return redirect('agregar_interes', pk)
    return render(request, 'agregar_encuesta.html', {'form': form})


def agregar_interes(request, pk):  #todo: ok
    form = InteresesForm()
    if request.method == 'POST':
        encuesta = Encuesta.objects.get(id=pk)
        form = InteresesForm(request.POST)
        if form.is_valid():
            interes = form.save(commit=False)
            interes.encuesta = encuesta
            interes.save()
            return redirect('agregar_interes', pk)
    return render(request, 'agregar_interes.html', {'form': form, 'pk': pk})


def editar_interes(request, id_i, pk):  #todo: ok
        interes = get_object_or_404(Intereses, id=id_i)
        form = InteresesForm(instance=interes)
        if request.method == "POST":
            form = InteresesForm(request.POST, instance=interes)
            if form.is_valid():
                form.save()
                return redirect('mis_intereses', pk)
        return render(request, 'editar_interes.html', {'form': form, 'pk': pk})


def eliminar_interes(request, id_i, pk):  #todo: ok
    interes_temp = Intereses.objects.get(id=id_i).delete()
    return redirect('mis_intereses', pk)


def mis_intereses(request, pk):  #todo: ok
    encuesta = Encuesta.objects.get(id=pk)
    intereses = Intereses.objects.filter(encuesta__id=encuesta.pk)
    return render(request, 'mis_intereses.html', {'intereses': intereses, 'pk': pk})


class ReporteEncuestaPDF(View):  #todo: ok
    def get(self, request, pk):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename = encuesta {}.pdf'.format(pk)
        document = SimpleDocTemplate(response, pagesize=pagesizes.landscape(pagesizes.LETTER), ) # portrait
        story = []

        story.append(self.tabla(pk))
        document.build(story)  #, onFirstPage=aa, onLaterPages=aa
        return response

    def tabla(self, pk):
        titulo = ['ENCUESTA', '', '', '', '']
        encabezado_encuesta = ('NOMBRE', 'EDAD', 'SEXO', 'GRADO DE ESCOLARIDAD', 'PESO CORPORAL')
        encabezado_interes = ['INTERESES', '', '', '', '']
        encuesta = Encuesta.objects.get(id=pk)
        intereses = Intereses.objects.filter(encuesta__id=encuesta.pk)
        encuesta_detalles = [encuesta.nombre, encuesta.edad, encuesta.sexo, encuesta.grado_escolaridad, encuesta.peso_corporal]
        intereses_detalles = [(i.intereses_personales,) for i in intereses]
        detalle_orden = Table([titulo] + [encabezado_encuesta] + [encuesta_detalles] + [encabezado_interes] + intereses_detalles)
        detalle_orden.setStyle(TableStyle([
            ('ALIGN', (0, 0), (4, 0), 'CENTER'),
            ('ALIGN', (0, 3), (4, 3), 'CENTER'),
            ('BACKGROUND', (0, 0), (4, 0), colors.aqua),
            ('BACKGROUND', (0, 1), (4, 1), colors.limegreen),
            ('BACKGROUND', (0, 3), (4, 3), colors.aqua),
            ('SPAN', (0, 0), (4, 0)),
            ('SPAN', (0, 3), (4, 3)),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
        ]))
        return detalle_orden