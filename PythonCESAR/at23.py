"""Atividade 23
- Façam um programa que imprima os valores da lista abaixo sem repetição de itens.

lista = [2,3,3,2,3,4,5,6,4,6,7,8,9,33,5,7,8,0,22,44,55,77,55,44,5566,55,3322,22]"""

lista = [2,3,3,2,3,4,5,6,4,6,7,8,9,33,5,7,8,0,22,44,55,77,55,44,5566,55,3322,22]
x = []
for l in lista:
    if l not in x:
        x.append(l)
print(x)
