"""Faça um Programa que peça um número inteiro e determine se ele é par ou impar."""


def par_ou_impar():
    try:
        numero = int(input('Digite um número inteiro: '))
        print('Par') if numero % 2 == 0 else print('Ímpar')
    except ValueError:
        print('Número inválido')


if __name__ == '__main__':
    par_ou_impar()
