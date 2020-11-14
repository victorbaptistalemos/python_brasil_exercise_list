"""Altere o programa de cálculo dos números primos,
informando, caso o número não seja primo, por quais número ele é divisível."""


def calcula_primo(n):
    lista_divisores = []

    try:
        n = int(n)
        if n < 0:
            raise ValueError()
        elif n <= 1:
            print(f'{n} não atende aos requisitos mínimos para ser número primo')
            return
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                lista_divisores.append(i)
        lista_divisores.append(n)
        if len(lista_divisores) == 2:
            print(f'{n} é um número primo')
        else:
            print(f'{n} não é um número primo, pois {n} é divisível por ', end='')
            for i in lista_divisores:
                if i == n:
                    print(' e ', end='')
                elif not i == 1:
                    print(', ', end='')
                print(i, end='')
    except ValueError:
        print('Você não informou um número natural para cálculo')


def numero_primo():
    print('Informe um número para calcular se é ou não primo')
    print('Para ser primo tem que ser um número natural com 2 divisores (1 e ele mesmo)')
    n = input('Qual número deseja calcular: ')
    calcula_primo(n)


if __name__ == '__main__':
    numero_primo()
