from django.db import models

class Agendamento(models.Model):
    dataHorario = models.DateTimeField()
    nomeCliente = models.CharField(max_length=256)
    emailCliente = models.EmailField()
    telefoneCliente = models.CharField(max_length=11)
