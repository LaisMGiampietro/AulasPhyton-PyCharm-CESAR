"""Atividade 45
Façam uma função que receba 3 números inteiros do usuário e retorne o maior entre eles."""


def maior(n1, n2, n3):
    resultado = n1
    if n2 > n1 and n2 > n3:
        resultado = n2
    if n3 > n1 and n3 > n2:
        resultado = n3
    return resultado


print(maior(int(input("Escreva o primeiro numero ")), int(input("Escreva o segundo numero ")), int(input("Escreva o terceiro numero "))))
