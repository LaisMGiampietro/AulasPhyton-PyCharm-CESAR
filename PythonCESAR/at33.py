"""Atividade 33

- Façam um programa que imprima todos os números primos entre 25 e 50 utilizando dois for loops."""

for x in range(25, 51):
    for n in range(2, x):
        if (x % n) == 0:
            break
        else:
            print(x)
