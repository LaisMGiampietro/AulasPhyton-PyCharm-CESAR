"""Atividade 40
- Façam um programa que calcule o produto dos valores do dicionário abaixo.
dicionario = {'n1':100,'n2':-54,'n3':247}"""

dicionario = {'n1': 100, 'n2': -54, 'n3': 247}
resultado = 1
for chave in dicionario:
  resultado = resultado * dicionario[chave]
print(resultado)
