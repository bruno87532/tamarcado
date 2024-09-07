from django.urls import path
from agenda.views import agendamentosDetail, agendamentoList
urlpatterns = [
    path("agendamentos/", agendamentoList, name="agendamentoList"),
    path("agendamentos/<int:id>/", agendamentosDetail, name="agendamentosDetail"),
]