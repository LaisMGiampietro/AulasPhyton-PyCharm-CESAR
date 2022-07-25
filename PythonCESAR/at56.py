"""Atividade 56
- Façam uma classe Carro com:
- Atributos:marca, ano e preço
Métodos: mostrar_preço e mostrar_informações(mostrar todos os atributos do carro)"""


class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        print(f'R$ {self.preco}')

    def mostrar_informacoes(self):
        print(self.marca, self.ano, self.preco)


carro = Carro("Ford", 64, 30000)
carro.mostrar_preco()
carro.mostrar_informacoes()
