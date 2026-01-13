# consultorio/forms.py

from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__' # Esto agarra TODOS los campos que tengas en models.py

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
