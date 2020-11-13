"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de crescimento."""


def tempo_de_crescimento(populacao_a, taxa_a, populacao_b, taxa_b):
    anos = 0

    while populacao_a < populacao_b:
        populacao_a *= 1 + taxa_a
        populacao_b *= 1 + taxa_b
        anos += 1

    return anos


def taxa_de_crescimento():
    taxa_a = 0.03
    taxa_b = 0.015
    populacao_a = 80_000
    populacao_b = 200_000

    print(tempo_de_crescimento(populacao_a, taxa_a, populacao_b, taxa_b))


if __name__ == '__main__':
    taxa_de_crescimento()
