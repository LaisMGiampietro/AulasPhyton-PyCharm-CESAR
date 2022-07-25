"""Atividade 46
• Façam uma função que retorna a quantidade de vogais e consoantes de uma palavra."""


def vogcons(palavra):
    vog = 0
    con = 0
    for letra in palavra:
        if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
            vog += 1
        else:
            con += 1
    return vog, con


print(vogcons("Paralelepipedo"))
