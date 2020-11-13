"""Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50"""


def imprimir_impares(inicio, fim):
    for i in range(inicio, fim):
        if i % 2 != 0:
            print(i)


if __name__ == '__main__':
    imprimir_impares(1, 50)
