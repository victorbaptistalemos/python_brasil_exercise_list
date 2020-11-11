"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
    os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais.
    Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; """


def raizes_equacao_quadratica():
    """ax²+bx+c=0"""

    try:
        a = int(input('Digite o valor de "a" (ax²): '))
        if a == 0:
            raise ValueError
        b = int(input('Digite o valor de "b" (bx): '))
        c = int(input('Digite o valor de "c" (c): '))
    except ValueError:
        print("Não é possível calcular uma equação quadrática com o valor informado")
        return

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Não há raízes para essa equação")
    elif delta == 0:
        x = - b / 2 * a
        print(f'A equação retornou uma raiz: x = {x}')
    else:
        x_1 = - b + delta ** 0.5
        x_2 = - b - delta ** 0.5
        print(f'A equação retornou duas raízes: x\' = {x_1} e x\'\' = {x_2}')


if __name__ == '__main__':
    raizes_equacao_quadratica()
