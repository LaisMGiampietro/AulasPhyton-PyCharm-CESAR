"""Atividade 13
- Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. 'Escolha a opção:
- 1- Soma de 2 números.
- 2- Diferença entre 2 números (maior pelo menor).
- 3- Produto entre 2 números.
- 4- Divisão entre 2 números (o denominador não pode ser zero).'
- dica vocês podem pular a linha em um print usando \n"""

print('Escolha a opção:\n1- Soma de 2 números.\n2- Diferença entre 2 números (maior pelo menor).\n3- Produto entre 2 números.\n4- Divisão entre 2 números (o denominador não pode ser zero).\n')
num = int(input('Opção escolhida:'))

while num < 0 or num > 4:
    print('Opção invalida!')
    num = int(input('Opção escolhida:'))

num1 = int(input('Num1:'))
num2 = int(input('Num2:'))

Soma = num1 + num2
diferenca = num1 - num2
diferenca2 = num2 - num1
produto = num1 * num2

if num == 1:
    print(f'Operação:{num1} + {num2} = {Soma} ')
if num == 2:
    if num1 > num2:
        print(f'Operação:{num1} - {num2} = {diferenca}')
    else:
        print(f'Operação:{num2} - {num1} = {diferenca2}')
if num == 3:
    print(f'Operação:{num1} * {num2} = {produto} ')
if num == 4:
    while num2 == 0:
        print('Denominador nao pode ser igual a zero!')
        num2 = int(input('Num2:'))
    else:
        divisao = num1 / num2
        print(f'Operação:{num1} / {num2} = {divisao}')
        