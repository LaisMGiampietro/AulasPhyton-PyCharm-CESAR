"""Atividade 37

Façam um programa que receba uma chave do usuário e cheque se ela pertence ao dicionário abaixo.
dicionario= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dicionario = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
valor = int(input("Digite um valor de chave:"))
if valor in dicionario:
    print("Pertence ao dicionario")
else:
    print("Chave não encontrada no dicionario")
  