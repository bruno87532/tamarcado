from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(http_method_names=["GET", "PUT"])
def agendamentosDetail(request, id):
    if request.method == "GET":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == "PUT":
        obj = get_object_or_404(Agendamento, id=id)
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            validatedData = serializer.validated_data
            obj.dataHorario = validatedData.get("dataHorario", obj.dataHorario)
            obj.nomeCliente = validatedData.get("nomeCliente", obj.nomeCliente)
            obj.emailCliente = validatedData.get("emailCliente", obj.emailCliente)
            obj.telefoneCliente = validatedData.get("telefoneCliente", obj.telefoneCliente)
            return JsonResponse(validatedData, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(http_method_names=["GET", "POST"])
def agendamentoList(request):
    if request.method == "GET":
        qs = Agendamento.objects.all()
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False )
    if request.method == "POST":
        data = request.data  
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            validatedData = serializer.validated_data
            Agendamento.objects.create(
                dataHorario = validatedData["dataHorario"],
                nomeCliente = validatedData["nomeCliente"],
                emailCliente = validatedData["emailCliente"],
                telefoneCliente = validatedData["telefoneCliente"],
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)