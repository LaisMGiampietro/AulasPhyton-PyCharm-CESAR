"""Atividade 15
Façam um programa que receba um valor do usuário e faça a contagem regressiva dele até o zero."""

valor = int(input('Numero:'))
while valor >= 0:
    print(valor)
    valor -= 1
    