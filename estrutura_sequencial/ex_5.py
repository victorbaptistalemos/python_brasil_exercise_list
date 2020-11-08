"""Faça um Programa que converta metros para centímetros."""


def metro_para_centimetro(s):
    """Converte um número em metros retorna seu valor em centímetros

    >>> metro_para_centimetro(1)
    100
    >>> metro_para_centimetro(0)
    0

    :param s: string
    :return: integer
    """

    return int(s) * 100


if __name__ == '__main__':
    print(metro_para_centimetro(1))
    print()
    print(metro_para_centimetro(0))
