class Aluno:
    def __init__(self, nome: str, notas: list, faltas: int = 0):
        self.nome = nome
        self.notas = notas
        self.faltas = faltas

    def calcular_media(self) -> float:
        return sum(self.notas) / len(self.notas)

    def situacao(self) -> str:
        if self.calcular_media() >= 6.0:
            return "Aprovado"
        return "Reprovado"

    def maior_nota(self) -> float:
        return max(self.notas)

    def menor_nota(self) -> float:
        return min(self.notas)

    def calcular_media_arredondada(self) -> float:
        return round(sum(self.notas) / len(self.notas))

    def situacao_final(self, total_aulas: int) -> str:
        percentual_faltas = self.faltas / total_aulas
        if percentual_faltas > 0.25:
            return "Reprovado por falta"
        if self.calcular_media() >= 6.0:
            return "Aprovado"
        return "Reprovado por nota"

    def enviar_boletim(self, email_service) -> None:
        if self.situacao() == "Reprovado":
            email_service.enviar(self.nome, self.calcular_media())


def contar_aprovados(alunos: list) -> int:
    return sum(1 for aluno in alunos if aluno.situacao() == "Aprovado")
