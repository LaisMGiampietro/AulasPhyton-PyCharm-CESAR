"""Atividade 29

- Façam um programa que adiciona os itens do conjunto 2 ao conjunto 1 se o item não for repetido.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.difference_update(set2)
for x in set1:
    set2.add(x)
print(set2)
