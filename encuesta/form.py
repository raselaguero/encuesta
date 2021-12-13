from .models import Encuesta, Intereses
from django.forms import ModelForm, inlineformset_factory


class EncuestaForm(ModelForm):
    class Meta:
        model = Encuesta
        fields = '__all__'


class InteresesForm(ModelForm):
    class Meta:
        model = Intereses
        fields = ['intereses_personales']
