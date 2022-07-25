"""Atividade 10

• Façam um Programa que leia três números e que imprima o maior e o menor."""

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
n3 = int(input('Informe o terceiro numero: '))

list = [n1, n2, n3]

print(f'O maior numero digitado foi: {max(list)} ')
print(f'O menor numero digitado foi: {min(list)} ')
