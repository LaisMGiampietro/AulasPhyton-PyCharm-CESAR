"""Atividade 49
Façam uma função que receba uma lista e embaralhe seus
elementos utilizando random.shuffle().
random.shuffle(x) embaralha os itens de x."""

import random

nums = [1, 2, 3, 4, 5]
print(nums)


def lista(l):
    random.shuffle(l)
    print(nums)


lista(nums)
