"""Atividade 12

• Façam um Programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km,
e R$ 0,45 para viagens mais longas."""

distancia = float(input('Distância a ser percorrida em km: '))
p_passagem = distancia * 0.50
p_passagem2 = distancia * 0.45
if distancia <= 200:
    print(f'Preço da passagem: {p_passagem}')
else:
    print(f'Preço da passagem: {p_passagem2}')
    