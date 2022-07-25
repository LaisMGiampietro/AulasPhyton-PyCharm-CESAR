"""Atividade 5

• Faça um programa que receba o faturamento e o custo de uma venda, calcule o lucro e depois
calcule e imprima a margem de lucro(lucro/ faturamento) com somente duas casas decimais."""

Faturamento = float(input('Digite o faturamento:'))
Custo_de_venda = float(input('Digite o custo de venda:'))

Lucro = Faturamento - Custo_de_venda

margem = Lucro / Faturamento

print(f'Margem de lucro: {margem:.2f}')
