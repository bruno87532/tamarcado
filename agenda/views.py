from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics

# Create your views here.

class AgendamentoList(generics.ListCreateAPIView):

    queryset = Agendamento.objects.filter(canceladoCliente=False)
    serializer_class = AgendamentoSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset = Agendamento.objects.filter(prestador__username = username)
        return queryset

class AgendamentosDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
