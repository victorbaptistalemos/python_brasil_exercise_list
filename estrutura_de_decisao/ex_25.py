"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente"."""


def cena_do_crime():
    contador = 0
    resposta = ''
    while resposta != 'S' and resposta != 'N':
        resposta = str.upper(input('Telefonou para a vítima? [S/n] '))
        if resposta == 'S':
            contador += 1

    resposta = ''

    while resposta != 'S' and resposta != 'N':
        resposta = str.upper(input('Esteve no local do crime? [S/n] '))
        if resposta == 'S':
            contador += 1

    resposta = ''

    while resposta != 'S' and resposta != 'N':
        resposta = str.upper(input('Mora perto da vítima? [S/n] '))
        if resposta == 'S':
            contador += 1

    resposta = ''

    while resposta != 'S' and resposta != 'N':
        resposta = str.upper(input('Devia para a vítima? [S/n] '))
        if resposta == 'S':
            contador += 1

    resposta = ''

    while resposta != 'S' and resposta != 'N':
        resposta = str.upper(input('Já trabalhou com a vítima? [S/n] '))
        if resposta == 'S':
            contador += 1

    print('Você é', end=' ')
    if contador == 5:
        print('o assassino')
    elif 2 < contador < 5:
        print('cúmplice')
    elif contador == 2:
        print('suspeito')
    else:
        print('inocente')


if __name__ == '__main__':
    cena_do_crime()
