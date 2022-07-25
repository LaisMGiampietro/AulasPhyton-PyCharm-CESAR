nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
nota3 = float(input("Terceira nota:"))
nota4 = float(input("Quarta nota:"))

media = nota2 + nota1 + nota3 + nota4 / 4

if media >= 7:
    print(f"Nota:{media}! \n Aprovado (=")
else:
    print(f"Nota:{media}! \n Reprovado )=")
