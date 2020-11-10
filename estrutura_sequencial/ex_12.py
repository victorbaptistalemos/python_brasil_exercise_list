"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58"""


def peso_ideal(h):
    """Utiliza a fórmula (72.7 * h) - 58 para calcular o peso ideal"""

    return 72.7 * float(h) - 58


if __name__ == '__main__':
    print(peso_ideal(input('Digite sua altura em metros ("1.70"): ')))
