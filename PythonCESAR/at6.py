"""Atividade 6
Façam um programa que pergunta a idade do usuário. Se o usuário não for menor de idade,
exiba uma mensagem de boas vindas. Caso o contrário, exiba uma mensagem informando que
não é permitido menores de idade no estabelecimento."""

Idade = int(input('Qual sua idade:'))

if Idade >= 18:
    print('Seja bem vindo!')
else:
    print('Não é permitido a participação de menores de idade!')
    