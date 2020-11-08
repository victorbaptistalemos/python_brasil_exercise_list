"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""


def celsius_to_fahrenheit(s):
    """Transforma a temperatura Celsius (°C) em  Fahrenheit (°F)

    >>> celsius_to_fahrenheit(-40)
    -40.0
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(30)
    86.0

    :param s: string
    :return: float
    """

    return 32 + ((9 * float(s)) / 5)


if __name__ == '__main__':
    print(celsius_to_fahrenheit(input("Digite a temperatura em Celsius (°C): ")))
