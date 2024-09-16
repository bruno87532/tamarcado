from django.urls import path
from agenda.views import AgendamentosDetail, AgendamentoList
urlpatterns = [
    path("agendamentos/", AgendamentoList.as_view(), name="AgendamentoList"),
    path("agendamentos/<int:pk>/", AgendamentosDetail.as_view(), name="AgendamentosDetail"),
]