"""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""


import math


def area_circulo(s):
    """Retorna o valor da área de um círculo"""

    return 0 if s == '' else math.pi * float(s) ** 2


if __name__ == '__main__':
    print(f'A área do círculo é: {area_circulo(input("Digite o valor do raio: "))}')
