"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo."""


def calculos_variados():
    """Realiza cálculos variados a partir da digitação de 3 valores"""

    primeiro = input("Digite o primeiro valor (inteiro): ")
    primeiro = 0 if primeiro == '' else int(primeiro)
    segundo = input("Digite o segundo valor (inteiro): ")
    segundo = 0 if segundo == '' else int(segundo)
    terceiro = input("Digite o terceiro valor (número real): ")
    terceiro = 0 if terceiro == '' else float(terceiro)

    print(f'O produto do dobro do primeiro com metade do segundo é {primeiro * (segundo / 2)}')
    print(f'A soma do triplo do primeiro com o terceiro é {3 * primeiro  + terceiro}')
    print(f'O terceiro elevado ao cubo é {terceiro ** 3}')


if __name__ == '__main__':
    calculos_variados()
