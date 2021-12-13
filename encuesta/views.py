from django.shortcuts import render, redirect
from .models import Encuesta, Intereses
from .form import EncuestaForm, InteresFormSet
from django.http import HttpResponse
from reportlab.platypus import TableStyle, SimpleDocTemplate, Table
from reportlab.lib import colors, pagesizes
from django.views.generic import View

# Create your views here.


def inicio(request):  #todo: ok
    return render(request, 'inicio.html')


def agregar_interes_formset(request, pk):
    encuesta = Encuesta.objects.get(id=pk)
    if request.method == 'POST':
        formset = InteresFormSet(request.POST, instance=encuesta)
        if formset.is_valid():
            formset.save()
            return redirect('agregar_interes_formset', pk)
    formset = InteresFormSet(instance=encuesta)
    return render(request, 'agregar_formset.html', {'formset': formset, 'pk': pk})


def agregar_encuesta(request):  #todo: ok
    form = EncuestaForm()
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            encuesta = form.save()
            pk = encuesta.id
            return redirect('agregar_interes_formset', pk)
    return render(request, 'agregar_encuesta.html', {'form': form})


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