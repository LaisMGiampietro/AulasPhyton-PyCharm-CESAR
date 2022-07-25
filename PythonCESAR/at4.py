"""Atividade 4

 Façam um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
     #- o produto do dobro do primeiro com metade do segundo .
     #- a soma do triplo do primeiro com o terceiro.
     #- o terceiro elevado ao cubo."""

n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Digite o segundo numero inteiro:'))
n3 = float(input('Digite um numero real:'))

print("Produto:", ((2*n1) * (n2/2)))
print("Soma:", (3 * n1) + n3)
print("Cubo:", n3**3)
