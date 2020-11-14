"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

from math import floor, sqrt


def calcula_primo(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError()
        lista_divisores = []
        lista_divisores.extend(range(2, n + 1))

        for index in range(2, floor(sqrt(n) + 1)):
            for number in lista_divisores:
                if number % index == 0:
                    lista_divisores.remove(number)
        return True if n in lista_divisores else False
    except ValueError:
        return None


def resposta_primo(n):
    resposta = calcula_primo(n)
    if resposta is None:
        print('Você não informou um número natural para cálculo')
    elif resposta:
        print(f'{n} é um número primo')
    else:
        print(f'{n} não é um número primo')


def numero_primo():
    print('Informe um número para calcular se é ou não primo')
    print('Para ser primo tem que ser um número natural com 2 divisores (1 e ele mesmo)')
    n = input('Qual número deseja calcular: ')
    resposta_primo(n)


if __name__ == '__main__':
    numero_primo()
