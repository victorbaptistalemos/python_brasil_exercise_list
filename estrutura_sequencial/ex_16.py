"""Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

from math import ceil as ceil


def total_de_latas_de_tinta(metragem):
    """Retorna a quantidade de lata(s) de tinta necessária(s) e o preço total.
     Considerando que cada litro de tinta cobre 3m².
     Considerando que cada lata de tinta contém 18 litros.
     Considerando que cada lata custa R$ 80.0"""

    metragem = 0 if metragem == '' else float(metragem)
    latas = ceil(metragem / 3 / 18)

    print(f'Para cobrir {metragem} m² será necessário {latas} lata(s) de tinta e preço total é de R$ {latas * 80.0}')


if __name__ == '__main__':
    total_de_latas_de_tinta(input("Informe a metragem a ser pintada: "))
