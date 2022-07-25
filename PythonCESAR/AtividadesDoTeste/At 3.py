aluguel = float(input("Digite seu aluguel aqui:"))
data_entrada = int(input("Digite aqui o ano de entrada:"))

depois = aluguel * 1.18
antes = aluguel * 1.15

if data_entrada > 2015:
    print(f"Valor com reajuste:{depois}")
else:
    print(f"Valor com reajuste:{antes}")
