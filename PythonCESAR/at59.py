"""Crie uma classe chamada Circulo que tenha um raio privado e as seguintes funções:
1. Mudar raio
2. Retornar raio
3. Cálculo e retorno do diâmetro
4. Cálculo e retorno da circunferência"""

import math


class Circulo:
    def __init__(self, __raio):
        self.__raio = __raio

    def mudar(self, __raio):
        self.__raio = __raio

    def retornar(self):
        return self.__raio

    def diametro(self):
        return 2 * self.__raio

    def circunferencia(self):
        return 2 * math.pi * self.__raio


"""Crie uma classe chamada Retangulo que possua um ladoA e um ladoB (horizontal e vertical respectivamente),
ambos privados.
A classe Retangulo deve possuir as seguintes funções:
1. Uma função para mudar e outra para retornar cada lado (A&B)
2. Cálculo da área
3. Cálculo do perímetro"""


class Retangulo:
    def __init__(self, ladoa, ladob):
        self.__ladoa = ladoa
        self.__ladob = ladob

    def mudara(self, __ladoa):
        self.__ladoa = __ladoa

    def mudarb(self, __ladob):
        self.__ladob = __ladob

    def retornara(self):
        return self.__ladoa

    def retornarb(self):
        return self.__ladob

    def area(self):
        return self.__ladoa * self.__ladob

    def perimetro(self):
        return 2 * (self.__ladoa + self.__ladob)


circulo = Circulo(2)
retangulo = Retangulo(50, 30)

"""Crie uma função chamada quantos_circulos que recaba um círculo e um retângulo 
#e calcule quantos círculos cabem em um retângulo.
#Ex.:
 _____
#|OOOOO| 
#|OOOOO|	----> 15 círculos
#|OOOOO|
#^^^^^^^  """


def quantos_circulos(retangulo, circulo):
    qtd_horizontal = 0
    qtd_vertical = 0

    ladoa = retangulo.retornara()
    ladob = retangulo.retornarb()

    # Horizontal
    while circulo.diametro() * (qtd_horizontal + 1) <= ladoa:
        qtd_horizontal += 1

    # Vertical
    while circulo.diametro() * (qtd_vertical + 1) <= ladob:
        qtd_vertical += 1

    total = qtd_horizontal * qtd_vertical
    resultado = (qtd_horizontal, qtd_vertical, total)

    return resultado


circ = Circulo(5)
rect = Retangulo(156, 123)

resultado = quantos_circulos(rect, circ)
print(f'Hor.: {resultado[0]}, Ver.: {resultado[1]}, Total: {resultado[2]}')
