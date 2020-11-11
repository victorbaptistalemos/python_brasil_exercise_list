"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

from datetime import datetime


def data_valida(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        print('Você digitou uma data válida')
    except ValueError:
        print('Você digitou uma data inválida')


if __name__ == '__main__':
    data_valida(input('Digite uma data no formato dd/mm/yyyy: '))
