"""Atividade 11
• Façam um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, de 15%."""

salario = float(input('Digite seu salário: '))
a_1 = salario * 0.10 + salario
a_2 = salario * 0.15 + salario
if salario <= 1250.00:
    print(f'Seu novo salário será de: {a_2 }')
else:
    print(f'Seu novo salário será de: {a_1}')
