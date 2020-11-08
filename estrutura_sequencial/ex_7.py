"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. """


def dobro_area(s):
    """Dobra a área recebida

    >>> dobro_area(1)
    2.0
    >>> dobro_area(2)
    8.0

    :param s: string
    :return: float
    """

    return 2 * area_quadrado(s)


def area_quadrado(s):
    """Calcula a área de um quadrado

    >>> area_quadrado(1)
    1.0
    >>> area_quadrado(2)
    4.0

    :param s: string
    :return: float
    """

    return float(s) ** 2


if __name__ == '__main__':
    print(dobro_area(input("Digite o valor do lado do quadrado: ")))
