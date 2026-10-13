nunber = int(input("Digite um número: "))
if nunber > 0:
    print("O número é positivo")
else:
    print("O número é negativo")
if nunber % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
if nunber % 3 == 0:
    print("O número é divisível por 3")
else:
    print("O número não é divisível por 3")
if nunber % 5 == 0:
    print("O número é divisível por 5")
else:
    print("O número não é divisível por 5")
if -10 <= nunber <= 10:
    print("O número está no intervalo [-10, 10]")
else:
    print("O número não está no intervalo [-10, 10]")
