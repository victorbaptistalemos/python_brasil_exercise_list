"""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""


import math


def calcular_area(s):
    return 0 if s == '' else math.pi * float(s) ** 2


print(f'A área do círculo é: {calcular_area(input("Digite o valor do raio: "))}')
