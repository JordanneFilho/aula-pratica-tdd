import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno, contar_aprovados


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


# --- Bug 3: menor_nota retorna max(notas) em vez de min(notas) ---

def test_menor_nota(aluno_aprovado):
    # notas = [8, 9, 7, 8] -> a menor é 7
    assert aluno_aprovado.menor_nota() == 7


# --- Bug 4: calcular_media_arredondada usa int() (trunca) em vez de round() ---

def test_calcular_media_arredondada_aluno_reprovado(aluno_reprovado):
    # notas = [4, 3, 5, 4] -> soma 16 / 4 = 4.0 -> arredondado 4
    assert aluno_reprovado.calcular_media_arredondada() == 4


def test_calcular_media_arredondada_arredonda_para_cima_corretamente():
    aluno = Aluno(nome="Ana", notas=[7, 8, 8])
    # soma 23 / 3 = 7.666... -> arredondado deveria ser 8 (int() trunca para 7)
    assert aluno.calcular_media_arredondada() == 8

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função

def test_contar_aprovados_todos_aprovados():
    alunos = [
        Aluno(nome="A", notas=[8, 8, 8, 8]),
        Aluno(nome="B", notas=[9, 9, 9, 9]),
    ]
    assert contar_aprovados(alunos) == 2


def test_contar_aprovados_todos_reprovados():
    alunos = [
        Aluno(nome="A", notas=[3, 3, 3, 3]),
        Aluno(nome="B", notas=[2, 2, 2, 2]),
    ]
    assert contar_aprovados(alunos) == 0


def test_contar_aprovados_lista_mista():
    alunos = [
        Aluno(nome="A", notas=[8, 8, 8, 8]),
        Aluno(nome="B", notas=[3, 3, 3, 3]),
        Aluno(nome="C", notas=[7, 7, 7, 7]),
    ]
    assert contar_aprovados(alunos) == 2


def test_contar_aprovados_lista_vazia():
    assert contar_aprovados([]) == 0


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método

def test_situacao_final_reprovado_por_falta_mesmo_com_media_alta():
    aluno = Aluno(nome="Carlos", notas=[9, 9, 9, 9], faltas=15)
    # 15/40 = 37.5% de faltas > 25%
    assert aluno.situacao_final(total_aulas=40) == "Reprovado por falta"


def test_situacao_final_aprovado_poucas_faltas_media_alta():
    aluno = Aluno(nome="Maria", notas=[8, 9, 7, 8], faltas=2)
    # 2/40 = 5% de faltas
    assert aluno.situacao_final(total_aulas=40) == "Aprovado"


def test_situacao_final_reprovado_por_nota_poucas_faltas():
    aluno = Aluno(nome="João", notas=[4, 3, 5, 4], faltas=2)
    # 2/40 = 5% de faltas, mas media < 6.0
    assert aluno.situacao_final(total_aulas=40) == "Reprovado por nota"


def test_situacao_final_faltas_exatamente_vinte_e_cinco_por_cento_segue_para_media():
    aluno = Aluno(nome="Ana", notas=[8, 8, 8, 8], faltas=10)
    # 10/40 = 25% exatamente -> nao reprova por falta, segue para media (alta -> aprovado)
    assert aluno.situacao_final(total_aulas=40) == "Aprovado"


def test_situacao_final_faltas_pouco_acima_de_vinte_e_cinco_por_cento_reprovado_por_falta():
    aluno = Aluno(nome="Bruno", notas=[9, 9, 9, 9], faltas=11)
    # 11/40 = 27.5% > 25%
    assert aluno.situacao_final(total_aulas=40) == "Reprovado por falta"


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método

def test_enviar_boletim_aluno_reprovado_aciona_servico_de_email(aluno_reprovado):
    email_service = MagicMock()

    aluno_reprovado.enviar_boletim(email_service)

    email_service.enviar.assert_called_once_with(
        aluno_reprovado.nome, aluno_reprovado.calcular_media()
    )


def test_enviar_boletim_aluno_aprovado_nao_aciona_servico_de_email(aluno_aprovado):
    email_service = MagicMock()

    aluno_aprovado.enviar_boletim(email_service)

    email_service.enviar.assert_not_called()
