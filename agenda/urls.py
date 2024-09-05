from django.urls import path
from agenda.views import agendamentosDetail, agendamentoList
urlpatterns = [
    path("agendamentos/<int:id>", agendamentosDetail, name="agendamentosDetail"),
    path("agendamentos/", agendamentoList, name="agendamentoList")
]