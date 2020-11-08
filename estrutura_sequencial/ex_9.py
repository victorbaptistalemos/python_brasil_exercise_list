"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius."""


def fahrenheit_to_celsius(s):
    """Transforma a temperatura Fahrenheit (°F) em Celsius (°C)

    >>> fahrenheit_to_celsius(-40)
    -40.0
    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(86)
    30.0

    :param s: string
    :return: float
    """

    return 5 * ((float(s) - 32) / 9)


if __name__ == '__main__':
    print(fahrenheit_to_celsius(input("Digite a temperatura em Fahrenheit (°F): ")))
