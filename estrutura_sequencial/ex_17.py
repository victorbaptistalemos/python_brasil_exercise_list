"""Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

from math import ceil as ceil
from math import floor as floor


def total_de_latas_e_ou_galoes_de_tinta(metragem):
    """Retorna a quantidade de lata(s) e/ou galão(ões) de tinta necessária(s) e o preço total.
     Considerando que cada litro de tinta cobre 6m².
     Considerando que cada lata de tinta contém 18 litros.
     Considerando que cada galão de tinta contém 3.6 litros.
     Considerando que cada lata custa R$ 80.0
     Considerando que cada lata custa R$ 25.0

    >>> total_de_latas_e_ou_galoes_de_tinta(500.0)
    Metragem informada: 500.0
    Será necessário 5 lata(s) de tinta e preço total é de R$ 400.0
    Será necessário 24 galão(ões) de tinta e preço total é de R$ 600.0
    Misturando, 5 lata(s) e 1 galão(ões) e o preço total é 425.0
    >>> total_de_latas_e_ou_galoes_de_tinta(250)
    Metragem informada: 250.0
    Será necessário 3 lata(s) de tinta e preço total é de R$ 240.0
    Será necessário 12 galão(ões) de tinta e preço total é de R$ 300.0
    Misturando, 2 lata(s) e 3 galão(ões) e o preço total é 235.0

    :param metragem: string
    """

    metragem = 0 if metragem == '' else float(metragem)
    litros = metragem / 6
    latas = ceil(litros / 18)
    galoes = ceil(litros / 3.6)

    print(f'Metragem informada: {metragem}')
    print(f'Será necessário {latas} lata(s) de tinta e preço total é de R$ {latas * 80.0}')
    print(f'Será necessário {galoes} galão(ões) de tinta e preço total é de R$ {galoes * 25.0}')

    litros *= 1.1
    latas = floor(litros / 18)
    litros -= latas * 18
    galoes = ceil(litros / 3.6)
    print(f'Misturando, {latas} lata(s) e {galoes} galão(ões) e o preço total é {latas * 80.0 + galoes * 25.0}')


if __name__ == '__main__':
    total_de_latas_e_ou_galoes_de_tinta(input("Informe a metragem a ser pintada: "))
