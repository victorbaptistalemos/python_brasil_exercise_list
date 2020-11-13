"""Faça um programa que leia 5 números e informe a soma e a média dos números."""


def recolher_numeros():
    lista = []
    for i in range(5):
        i = int(input('Digite um número: '))
        lista.append(i)
    soma = 0
    for i in lista:
        soma += i
    media = soma / len(lista)

    return soma, media


def maior_numero():
    soma, media = recolher_numeros()
    print(f'A soma é: {soma}')
    print(f'A média é: {media}')


if __name__ == '__main__':
    maior_numero()
