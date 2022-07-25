"""Atividade 50
Façam uma função utilizando random.choice() que:
Guarde as lista abaixo em uma lista;
Selecione uma das listas abaixo;
Imprima um de seus elementos aleatoriamente;
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let = ["a", "b", "c", "d", "e"]
tf = [True,False,None]
random.choice(x) escolhe um item de x."""
import random

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let = ["a", "b", "c", "d", "e"]
tf = [True, False, None]


def listas(n, x, t):
    lista = [n, x, t]
    escolhido = random.choice(lista)
    print(random.choice(escolhido))


listas(num, let, tf)
