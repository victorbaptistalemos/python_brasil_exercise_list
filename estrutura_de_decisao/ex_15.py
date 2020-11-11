"""Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno."""


def receber_lados_triangulo():
    lado_1 = -1.0
    lado_2 = -1.0
    lado_3 = -1.0

    error = True
    while not lado_1 >= 0.0 or error:
        try:
            lado_1 = float(input("Digite o valor do primeiro lado do triângulo: "))
            error = False
        except ValueError:
            lado_1 = -1.0

    error = not error
    while not lado_2 >= 0.0 or error:
        try:
            lado_2 = float(input("Digite o valor do segundo lado do triângulo: "))
            error = False
        except ValueError:
            lado_2 = -1.0

    error = not error
    while not lado_3 >= 0.0 or error:
        try:
            lado_3 = float(input("Digite o valor do terceiro lado do triângulo: "))
            error = False
        except ValueError:
            lado_3 = -1.0

    return lado_1, lado_2, lado_3


def verificar_triangulo():
    lado_1, lado_2, lado_3 = receber_lados_triangulo()

    if lado_1 + lado_2 >= lado_3 and lado_1 + lado_3 >= lado_2 and lado_2 + lado_3 >= lado_1:
        if lado_1 == lado_2 == lado_3:
            resultado = 'Os valores informados formam um Triângulo Equilátero'
        elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
            resultado = 'Os valores informados formam um Triângulo Isóceles'
        else:
            resultado = 'Os valores informados formam um Triângulo Escaleno'
    else:
        resultado = 'Os valores informados não podem fazer um Triângulo'

    print(resultado)


if __name__ == '__main__':
    verificar_triangulo()
