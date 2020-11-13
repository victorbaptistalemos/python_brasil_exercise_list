"""Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro."""


def imprimir_abaixo(inicio, fim):
    while inicio <= fim:
        print(inicio, end='')
        inicio += 1
        if inicio <= fim:
            print(' ', end='')
    print()


if __name__ == '__main__':
    imprimir_abaixo(1, 20)
