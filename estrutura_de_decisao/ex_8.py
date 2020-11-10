"""Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""


def menor_entre_tres():
    """Solicita 3 valores e retorna o produto de menor valor entre eles"""

    produto_1 = float(input("Digite o preço do primeiro produto: "))
    produto_2 = float(input("Digite o preço do segundo produto: "))
    produto_3 = float(input("Digite o preço do terceiro produto: "))

    if produto_1 < produto_2 and produto_1 < produto_3:
        menor_produto = 'primeiro'
    elif produto_2 < produto_3:
        menor_produto = 'segundo'
    else:
        menor_produto = 'terceiro'

    print(f'Você deve comprar o {menor_produto} produto')


if __name__ == '__main__':
    menor_entre_tres()
