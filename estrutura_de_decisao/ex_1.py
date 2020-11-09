"""Faça um Programa que peça dois números e imprima o maior deles."""


def maior_numero(primeiro, segundo):
    """Retorna o maior número.

    >>> maior_numero(1, 2)
    2.0
    >>> maior_numero(2, 1)
    2.0

    :param primeiro: float
    :param segundo: float
    :return: float
    """
    primeiro = 0 if primeiro == '' else float(primeiro)
    segundo = 0 if segundo == '' else float(segundo)
    return primeiro if primeiro > segundo else segundo


if __name__ == '__main__':
    print(maior_numero(input("Insira o primeiro número: "), input("Insira o segundo número: ")))