from django.db import models

class Agendamento(models.Model):
    prestador = models.ForeignKey("auth.User", related_name="agendamentos", on_delete=models.CASCADE)

    dataHorario = models.DateTimeField()
    nomeCliente = models.CharField(max_length=256, blank=True)
    emailCliente = models.EmailField()
    telefoneCliente = models.CharField(max_length=11)
    canceladoCliente = models.BooleanField(default=False, null=True)