import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

# --- Bug 1: calcular_media divide por 4 fixo, em vez de len(notas) ---

def test_calcular_media_aluno_aprovado(aluno_aprovado):
    # notas = [8, 9, 7, 8] -> soma 32 / 4 notas = 8.0
    assert aluno_aprovado.calcular_media() == 8.0


def test_calcular_media_com_quantidade_de_notas_diferente_de_quatro():
    aluno = Aluno(nome="Pedro", notas=[10, 10, 10])
    # soma 30 / 3 notas = 10.0 (o bug usa /4 fixo e daria 7.5)
    assert aluno.calcular_media() == 10.0


# --- Bug 2: situacao usa "> 6.0", excluindo erroneamente a média exata 6.0 ---

def test_situacao_aluno_com_media_exatamente_seis_deve_ser_aprovado():
    aluno = Aluno(nome="Carlos", notas=[6, 6, 6, 6])
    assert aluno.situacao() == "Aprovado"

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
