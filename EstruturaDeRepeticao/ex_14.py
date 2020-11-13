"""Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares
e a quantidade de números impares"""


def pares_e_impares():
    lista = []
    contador = 0
    pares = 0
    impares = 0
    while contador < 10:
        numero = input(f'Insira o valor #{contador + 1}: ')
        try:
            numero = int(numero)
            lista.append(numero)
            contador += 1
        except ValueError:
            print('Valor inválido')
    for i in lista:
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    print()
    print(f'Quantidade de números pares: {pares}')
    print(f'Quantidade de números ímpares: {impares}')


if __name__ == '__main__':
    pares_e_impares()
