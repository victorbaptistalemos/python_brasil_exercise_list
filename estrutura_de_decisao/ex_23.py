"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal."""


def inteiro_ou_decimal():
    numero = input('Digite um número qualquer (real ou inteiro): ')

    try:
        numero = int(numero)
        print('O número digitado é inteiro')
        return
    except ValueError:
        pass

    try:
        numero = float(numero)
        print('O número digitado é decimal')
    except ValueError:
        print('Você não digitou um número')


if __name__ == '__main__':
    inteiro_ou_decimal()
