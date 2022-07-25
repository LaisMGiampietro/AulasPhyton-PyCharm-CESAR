"""Atividade 48
Façam uma função que:
Receba a quantidade de lados de um dado;
Imprima um valor aleatório de 1 até o número de
lados, utilizando a biblioteca random e a função
random.randint().
randint(a, b) retorna um número inteiro entre a e b."""

import random


def roll(lados):
    print(f"Você rolou um D{lados}! \nO resultado foi {random.randint(1,lados)}.")


roll(5)
