"""Atividade 32
- Façam um programa que imprima os inteiros de 1 a 50. Para múltiplos de três imprima "Fizz" em vez do número e para os múltiplos de cinco imprima "Buzz". Para números que são múltiplos de três e cinco, imprima "FizzBuzz"."""

for x in range(1, 51):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)
        