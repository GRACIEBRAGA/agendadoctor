# pacientes/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Consulta
from .forms import ConsultaForm


def homepage(request):
    return render(request, 'homepage.html')

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})

def detalhes_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    consultas = Consulta.objects.filter(paciente=paciente)
    return render(request, 'detalhes_paciente.html', {'paciente': paciente, 'consultas': consultas})

def nova_consulta(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.paciente = paciente
            consulta.save()
            return redirect('detalhes_paciente', pk=paciente.pk)
    else:
        form = ConsultaForm()
    return render(request, 'nova_consulta.html', {'form': form})


