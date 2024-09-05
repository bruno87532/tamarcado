from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(http_method_names=["GET"])
def agendamentosDetail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    serializer = AgendamentoSerializer(obj)
    return JsonResponse(serializer.data)

@api_view(http_method_names=["GET"])
def agendamentoList(request):
    qs = Agendamento.objects.all()
    serializer = AgendamentoSerializer(qs, many=True)
    return JsonResponse(serializer.data, safe=False )