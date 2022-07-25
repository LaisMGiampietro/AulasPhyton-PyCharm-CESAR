"""Atividade 51
Façam uma função que receba o ano de
nascimento do usuário, e retorne sua idade
utilizando datetime.date.today().year.
datetime.date.today().year retorna o ano atual."""

import datetime


def nascimento(ano):
    print(f"Idade:{datetime.date.today().year - ano}")


nascimento(int(input("Digite seu ano de nascimento:")))
