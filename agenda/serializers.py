from rest_framework import serializers

class AgendamentoSerializer(serializers.Serializer):
    dataHorario = serializers.DateTimeField(format="%d/%m/%Y %H:%M")
    nomeCliente = serializers.CharField(max_length=256)
    emailCliente = serializers.EmailField()
    telefoneCliente = serializers.CharField(max_length=11)