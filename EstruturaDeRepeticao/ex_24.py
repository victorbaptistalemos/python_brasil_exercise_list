"""Faça um programa que calcule o mostre a média aritmética de N notas."""


def cria_lista():
    print('Insira números para calcular a média, deixe o campo vazio para terminar:')
    lista = []
    entrada = -1
    while entrada != '':
        try:
            entrada = input('Insira um número: ')
            if entrada == '':
                continue
            entrada = float(entrada)
            lista.append(entrada)
        except ValueError:
            print('Você não digitou um valor válido')
    return lista


def media():
    lista = cria_lista()
    try:
        soma = 0
        for i in lista:
            soma += i
        print(f'A média é: {soma / len(lista):.3f}')
    except ZeroDivisionError:
        print('Não é possível efetuar divisão por 0')


if __name__ == '__main__':
    media()
