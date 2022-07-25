"""Atividade 17
Façam um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido"""

valor = int(input('Digite uma nota entre zero e dez:'))

while valor < 0 or valor > 10:
    print('Número inválido!')
    valor = int(input('Digite uma nota entre zero e dez:'))

print(f'Nota escolhida: {valor}')
