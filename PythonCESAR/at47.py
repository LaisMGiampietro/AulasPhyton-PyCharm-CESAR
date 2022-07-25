"""Atividade 47
- Façam uma função que receba dois números, e uma das opções abaixo como parâmetro:
Adição, subtração, multiplicação, divisão e exponenciação.
- De acordo com a operação recebida, a realize e retorne seu resultado."""


def calculos(n, n1, operacao):
    operacao = operacao
    if operacao == "adição":
        return n + n1
    if operacao == "subtração":
        return n - n1
    if operacao == "divisão":
        return n / n1
    if operacao == "multiplicação":
        return n * n1


print(calculos(5, 4, "multiplicação"))
