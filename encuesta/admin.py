from django.contrib import admin
from .models import Encuesta, Intereses
# Register your models here.


#@admin.register(Intereses)
class InteresesInline(admin.TabularInline):
    model = Intereses

@admin.register(Encuesta)
class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'sexo', 'grado_escolaridad', 'peso_corporal')
    inlines = [InteresesInline]


