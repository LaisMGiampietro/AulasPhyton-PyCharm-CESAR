"""Atividade 57
- Façam uma Aluno com:
- Atributos: nome, matricula, nota1, nota 2, nota3 e nota 4
Métodos: media( calcula e imprime a média do aluno) e ponto_extra(aumenta uma nota escolhida)"""


class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.notas = notas
        self.matricula = matricula

    def media(self):
        total = 0
        for i in range(0, len(self.notas)):
            total += self.notas[i]
        print(f'{self.nome} tem uma media de {total / len(self.notas) : .2f}')

    def ponto_extra(self, numero_nota, incremento):
        if numero_nota <= len(self.notas):
            self.notas[numero_nota - 1] += incremento
            return
        print("Nota nao existe.")


aluno = Aluno("Lais", 123456, [5, 6, 7, 8, 9])
aluno.media()
aluno.ponto_extra(3, 2)
aluno.media()
