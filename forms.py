# pacientes/forms.py

from django import forms
from .models import Paciente, Consulta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'telefone']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data_hora', 'motivo']
