from rest_framework import serializers
from agenda.models import Agendamento
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = "__all__"

    prestador = serializers.CharField()
    
    def validate_dataHorario(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Agendamento não pode ser feito no passado")
        return value
    
    def validate_prestador(self, value):
        try:
            user = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Prestador com este nome não encontrado")
        return user
    
    def validate(self, attrs):
        telefoneCliente = attrs.get("telefoneCliente", "")
        emailCliente = attrs.get("emailCliente", "")
        if telefoneCliente.startswith("+") and emailCliente.endswith(".br") and not telefoneCliente.startswith("+55"):
            raise serializers.ValidationError("O telefone e email devem ser brasileiros!")
        return attrs
