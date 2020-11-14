"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores"""


def maior_menor_soma(*args):
    lista = []
    for i in args:
        lista.append(i)
    lista.sort()
    if len(lista) > 0:
        menor = lista[0]
        maior = lista[len(lista) - 1]
        soma = 0
        for i in lista:
            soma += i

        print(f'Maior número da lista: {maior}')
        print(f'Menor número da lista: {menor}')
        print(f'Soma dos itens da lista: {soma}')
    else:
        print('Impossível calcular, lista vazia')


if __name__ == '__main__':
    maior_menor_soma(9, 4, 6, 2, 7, 8, 6, 1, 3, 5)
    print()
    maior_menor_soma(5)
    print()
    maior_menor_soma()
