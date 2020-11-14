"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados"""

from math import floor, sqrt


def mostrar_primos(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError()
        lista_primos = []
        lista_primos.extend(range(2, n + 1))

        for index in range(2, floor(sqrt(n) + 1)):
            for number in lista_primos:
                if number % index == 0:
                    if not number == index:
                        lista_primos.remove(number)
        return lista_primos
    except ValueError:
        return None


def resposta_primo(n):
    resposta = mostrar_primos(n)
    if resposta is None:
        print(f'Impossível calcular com {n} como argumento')
    elif len(resposta) == 0:
        print(f'O primeiro número primo é o número 2 e você informou {n}')
    elif len(resposta) == 1:
        print(f'{n} é o único número primo da lista')
    else:
        print(f'Segundo o crivo de Eratóstenes, foi necessário {floor(sqrt(int(n)) - 1)} divisões.')
        print(f'A lista de números primos entre 2 e {n} é: ', end='')
        for i in range(len(resposta)):
            if i == len(resposta) - 1 and not resposta[i] == 2:
                print(' e ', end='')
            elif not i == 0:
                print(', ', end='')
            print(resposta[i], end='')


def numero_primo():
    print('Informe um número natural maior que 2 para informar os números primos entre eles:')
    print('Para ser primo tem que ser um número natural com 2 divisores (1 e ele mesmo)')
    n = input('Qual número deseja calcular: ')
    resposta_primo(n)


if __name__ == '__main__':
    numero_primo()
