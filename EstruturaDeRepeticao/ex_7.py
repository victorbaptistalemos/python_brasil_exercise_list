"""Faça um programa que leia 5 números e informe o maior número. """


def recolher_numeros():
    lista = []
    for i in range(5):
        i = int(input('Digite um número: '))
        lista.append(i)
    lista.sort()
    return lista[len(lista) - 1]


def maior_numero():
    maior = recolher_numeros()
    print(f'O maior número é: {maior}')


if __name__ == '__main__':
    maior_numero()
