"""Atividade 38

- Façam um programa que unifique os dicionários abaixo em um terceiro dicionário.
dicionario1 = {'dez': 10, 'vinte': 20, 'trinta': 30}
dicionario2 = {'trinta': 30, 'quarenta': 40, 'cinquenta': 50}"""

dicionario1 = {'dez': 10, 'vinte': 20, 'trinta': 30}
dicionario2 = {'trinta': 30, 'quarenta': 40, 'cinquenta': 50}

dicionario3 = dicionario1.copy()
dicionario3.update(dicionario2)
print(dicionario3)
