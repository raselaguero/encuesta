from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

SEXO_CHOICES = [
    ('MASCULINO', 'MASCULINO'),
    ('FEMENINO', 'FEMENINO')
]

GRADO_CHOICES = [
    ('BACHILLER','BACHILLER'),
    ('LICENCIADO','LICENCIADO'),
    ('MASTER','MASTER'),
    ('DOCTOR','DOCTOR')
]

def validar_peso(valor):
    if valor <= 0:
        raise ValidationError('El peso no debe ser cero, ni tener valores negativos')

def validar_edad(valor):
    if valor < 0:
        raise ValidationError('La edad no debe ser cero')

class Encuesta(models.Model):
    nombre = models.CharField(max_length=50, unique=True, help_text='El nombre del usuario encuestado debe ser único')
    edad = models.PositiveIntegerField(validators=[validar_edad])
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    grado_escolaridad = models.CharField(max_length=10, choices=GRADO_CHOICES)
    peso_corporal = models.FloatField(validators=[validar_peso])

    def __str__(self):
        return '%s' % self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Encuestas'


class Intereses(models.Model):
    intereses_personales = models.CharField(max_length=100)
    encuesta = models.ForeignKey('Encuesta', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.intereses_personales

    class Meta:
        ordering = ['intereses_personales']
        verbose_name_plural = 'Intereses'