"""Atividade 36
Façam um programa que imprima as chaves e os valores do dicionário abaixo igual ao exemplo.
Dicionário:
computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250gb'}
Exemplo:
Chave = CPU e Valor = Intel"""

computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250gb'}
for chave in computador:
    print(f"Chave = {chave} e valor = {computador[chave]}")
