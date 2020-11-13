"""Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles"""


def imprimir_intervalo(inicio, fim):
    for i in range(inicio, fim + 1):
        print(i)


if __name__ == '__main__':
    imprimir_intervalo(1, 20)
