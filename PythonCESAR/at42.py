"""Atividade 42
Façam uma função que receba uma quantidade indeterminada de argumentos, e imprima seus valores."""


def variados(*args):
    for n in args:
        print(n)


variados(3, 4, 5)
