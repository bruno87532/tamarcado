from django.test import TestCase
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from rest_framework.test import APITestCase
from datetime import datetime, timezone
import json

class TestListaAgendamentos(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/agendamentos/")
        self.assertEqual(json.loads(response.content), [])
    def test_listagem_com_agendamentos(self):
        data_horario = datetime(2024, 9, 20, tzinfo=timezone.utc)
        agendamento = Agendamento(
            nomeCliente="Bruno",
            emailCliente="bruno@gmail.com",
            telefoneCliente="19982869853",
            dataHorario=data_horario
        )
        agendamento.save()
        serializer = AgendamentoSerializer(agendamento)
        response = self.client.get("/api/agendamentos/")
        response_data = json.loads(response.content)
        self.assertIn(serializer.data, response_data)

class TestAtualizaAgendamento(APITestCase):
    def test_atualiza_agendamento(self):
        Agendamento.objects.create(
            nomeCliente="Bruno",
            emailCliente="bruno@gmail.com",
            telefoneCliente="1998289853",
            dataHorario=datetime.now(timezone.utc)
        )
        response_patch = self.client.patch("/api/agendamentos/1/", {
            "dataHorario": "2024-09-20T20:00:00Z"
        }, format="json")
        self.assertEqual(response_patch.status_code, 200)
        response_get = self.client.get("/api/agendamentos/")
        response_data = json.loads(response_get.content)
        self.assertEqual(response_data[0]["dataHorario"], "2024-09-20T20:00:00Z")

class TestDeletandoAgendamento(APITestCase):
    def test_deleta_agendamento(self):
        Agendamento.objects.create(
            nomeCliente="Bruno",
            emailCliente="bruno@gmail.com",
            telefoneCliente="1998289853",
            dataHorario=datetime.now(timezone.utc)
        )
        response = self.client.delete("/api/agendamentos/1/")
        self.assertEqual(response.status_code, 204)

class TestCriandoAgendamento(APITestCase):
    def test_cria_agendamento(self):
        data_horario_iso = datetime(2024, 9, 20, tzinfo=timezone.utc)
        response = self.client.post("/api/agendamentos/", {
            "nomeCliente": "Bruno",
            "emailCliente": "bruno@gmail.com",
            "telefoneCliente": "999994444",
            "dataHorario": data_horario_iso           
        }, format="json")
        self.assertEqual(response.status_code, 201)
        agendamento = Agendamento.objects.get()
        self.assertEqual(agendamento.nomeCliente, "Bruno")
        self.assertEqual(agendamento.emailCliente, "bruno@gmail.com")
        self.assertEqual(agendamento.telefoneCliente, "999994444")
        self.assertEqual(agendamento.dataHorario, data_horario_iso)
    def test_cria_agendamento_com_post_e_get(self):
        data_horario_iso = "2024-09-20T16:00:00Z"
        response_post = self.client.post("/api/agendamentos/", {
            "nomeCliente": "Bruno",
            "emailCliente": "bruno@gmail.com",
            "telefoneCliente": "999994444",
            "dataHorario": data_horario_iso           
        }, format="json")
        self.assertEqual(response_post.status_code, 201)
        response_get = self.client.get("/api/agendamentos/")
        response_data = json.loads(response_get.content)
        self.assertEqual(response_data[0], {
            "id": 1,
            "nomeCliente": "Bruno",
            "emailCliente": "bruno@gmail.com",
            "telefoneCliente": "999994444",
            "dataHorario": data_horario_iso           
        })