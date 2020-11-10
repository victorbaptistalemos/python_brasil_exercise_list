"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius."""


def fahrenheit_to_celsius(s):
    """Transforma a temperatura Fahrenheit (°F) em Celsius (°C)"""

    return 5 * ((float(s) - 32) / 9)


if __name__ == '__main__':
    print(fahrenheit_to_celsius(input("Digite a temperatura em Fahrenheit (°F): ")))
