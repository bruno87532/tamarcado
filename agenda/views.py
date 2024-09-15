from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class AgendamentoList(APIView):
    def get(self, request):
        qs = Agendamento.objects.filter(canceladoCliente=False)
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False )
    def post(self, request):
        data = request.data  
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class AgendamentosDetail(APIView):
    def get(self, request, id):
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    def patch(self, request, id):
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    def delete(self, request, id):
        obj = get_object_or_404(Agendamento, id=id)
        obj.canceladoCliente = True
        obj.save()
        return Response(status=204)


