"""Atividade 9
• Façam um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h,
exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa,
cobrando R$ 5 por km acima de 80 km/h."""

velocidade = int(input('Velocidade do veiculo:'))
multa = (velocidade - 80) * 5

if velocidade > 80:
    print(f'Voce foi multado! Valor da multa R$ {multa}')
else:
    print('Não foi multado!')
