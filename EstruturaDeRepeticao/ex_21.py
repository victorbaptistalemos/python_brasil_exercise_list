"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1."""


def calcula_primo(n):
    contador = 0

    try:
        n = int(n)
        if n < 0:
            raise ValueError()
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                contador += 1
        return True if contador == 1 else False
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
