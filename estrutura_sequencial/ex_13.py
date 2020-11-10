"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
 utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7"""


def peso_ideal(h):
    """Utiliza as fórmulas (72.7 * h) - 58 e (62.1*h) - 44.7 para calcular o peso ideal"""

    print(f'Peso ideal para homens: {72.7 * float(h) - 58}')
    print(f'Peso ideal para mulheres: {62.1 * float(h) - 44.7}')


if __name__ == '__main__':
    peso_ideal(input('Digite sua altura em metros ("1.70"): '))
