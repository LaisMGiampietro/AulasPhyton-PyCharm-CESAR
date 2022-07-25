"""Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios."""


class Conta:
    def __init__(self, nome, numero, saldo=0):
        self.nome = nome
        self.saldo = saldo
        self.numero = numero

    def altera_nome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor
        print(f"Seu saldo com deposito é de {self.saldo}")

    def saque(self, valor):
        if self.saldo > 0 and self.saldo - valor >= 0:
            self.saldo -= valor
            print(f"Seu saldo com o saque é de {self.saldo}")
            return
        print(f'Nao ha saldo o suficiente para sacar R$ {valor}.')


conta = Conta(1648864, "Lais")
conta.deposito(30)
conta.saque(10)
