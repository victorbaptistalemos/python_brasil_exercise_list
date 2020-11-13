"""Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número"""


def potencia(base, expoente):
    base = int(base)
    expoente = int(expoente)
    print(base ** expoente)


if __name__ == '__main__':
    potencia(input('Insira o valor da base: '),
             input('Insira o valor do expoente: '))
