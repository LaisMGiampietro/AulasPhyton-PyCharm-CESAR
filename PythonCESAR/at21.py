"""Atividade 21
- Façam um programa que adicione 3 valores recebidos pelo usuário na lista abaixo.
lista = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(3):
    lista.append(int(input(f'Digite o {x + 1} número : ')))
print(lista)
