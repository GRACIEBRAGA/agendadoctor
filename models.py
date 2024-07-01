# pacientes/models.py

from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    motivo = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.paciente.nome} - {self.data_hora}'

