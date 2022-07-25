"""Atividade 7
• Façam um script que peça um valor e mostre na tela se o valor é positivo ou negativo,
caso o número seja zero, mostre que o número não é positivo e nem negativo."""

Valor = int(input('Digite um valor:'))

if Valor > 0:
    print('Positivo')
elif Valor == 0:
    print('Não é positivo nem negativo.')
else:
    print('Negativo')
