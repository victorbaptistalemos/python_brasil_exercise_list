"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. """


def dobro_area(s):
    """Dobra a área recebida"""

    return 2 * area_quadrado(s)


def area_quadrado(s):
    """Calcula a área de um quadrado"""

    return float(s) ** 2


if __name__ == '__main__':
    print(dobro_area(input("Digite o valor do lado do quadrado: ")))
