"""Atividade 16
- Façam um programa que receba um número inteiro e imprima a tabuada desse número até o 10.

Dica: Com o print formatado, vocês podem escrever múltiplas variáveis. Exemplo:
x = 1
y = 2
print(f"{x} + {y} = {x + y}") # resultado 1 + 2 = 3"""

n = int(input('Digite um numero inteiro:'))
tabuada = 0

while tabuada < 10:
    tabuada += 1
    print(f"{n} * {tabuada} = {tabuada * n}")
    