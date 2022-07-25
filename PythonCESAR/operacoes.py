def Somar(lista):
    total = 0
    for x in lista:
        total += x
    return total


def Subtrair(lista):
    total = lista[0] * 2
    for x in lista:
        total -= x
    return total


def Multiplicar(lista):
    total = 1
    for x in lista:
        total *= x
    return total


def Dividir(lista):
    total = 1
    for x in lista:
        total /= x
    return total
