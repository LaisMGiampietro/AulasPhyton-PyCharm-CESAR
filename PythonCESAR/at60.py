class Racional():
	def __init__(self, numerador, denominador):
		self.numerador = numerador
		self.denominador = denominador

	def inverter_sinal(self, r):
		r = Racional(-r.numerador, r.denominador)
		return r

	def somar_racionais(self, r1, r2):
		r = Racional((r1.numerador * r2.denominador) + (r2.numerador * r1.denominador),
		r2.denominador * r1.denominador)
		return r

	def subtrair_racionais(self, r1, r2):
		r = Racional((r1.numerador * r2.denominador) - (r2.numerador * r1.denominador),
		r2.denominador * r1.denominador)
		return r

	def produto_racionais(self, r1, r2):
		r = Racional(r1.numerador * r2.numerador, r1.denominador * r2.denominador)
		return r

	def quociente_racionais(self, r1, r2):
		r = Racional(r1.numerador * r2.denominador, r1.denominador * r2.numerador)
		return r.numerador/r.denominador


class BombaCombustivel:
	def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
		self.__tipoCombustivel = tipoCombustivel
		self.__valorLitro = valorLitro
		self.__quantidadeCombustivel = quantidadeCombustivel

	def abastecerPorValor(self, valor):
		litros = valor / self.__valorLitro
		if self.__quantidadeCombustivel - litros > 0:
			self.__quantidadeCombustivel -= litros
			print(f'Foram colocados {litros:.2f}L em seu veiculo.')
			return
		print(f'Nao ha combustivel suficiente na bomba para abastecer {litros:.2f}L.')
		print(f'Combustivel restante: {self.__quantidadeCombustivel:.2f}L.')

	def abastecerPorLitro(self, litros):
		if self.__quantidadeCombustivel - litros > 0:
			valor = litros * self.__valorLitro
			self.__quantidadeCombustivel -= litros
			print(f'Foram colocados {litros:.2f}L em seu veiculo.')
			print(f'Voce deve R${valor:.2f}.')
			return

		print(f'Nao ha combustivel suficiente na bomba para abastecer {litros:.2f}L.')
		print(f'Combustivel restante: {self.__quantidadeCombustivel:.2f}L.')

	def alterarValor(self, valor):
		self.__valorLitro = valor

	def alterarCombustivel(self, tipoCombustivel):
		self.__tipoCombustivel = tipoCombustivel

	def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
		self.__quantidadeCombustivel = quantidadeCombustivel


bomba = BombaCombustivel("Diesel", 4.57, 1280)
bomba.abastecerPorValor(38.95)
bomba.abastecerPorLitro(80)
bomba.alterarValor(0.01)
bomba.abastecerPorLitro(482.547)


