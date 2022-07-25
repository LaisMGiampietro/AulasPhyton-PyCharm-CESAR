"""Atividade 24

- Façam um programa que adiciona os itens da segunda lista na primeira lista e imprima a primeira lista.

lista1 = [23, 24, 25, 26]
lista2 = [27, 28, 29, 30]"""

lista1 = [23, 24, 25, 26]
lista2 = [27, 28, 29, 30]

for x in lista2:
    lista1.append(x)
print(lista1)
