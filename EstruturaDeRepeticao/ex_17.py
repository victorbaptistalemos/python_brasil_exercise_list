"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""


def fatorial(n):
    try:
        n = int(n)
        resposta = 1
        if n < 0:
            raise UserWarning(f'Não é possivel calcular {n}!, uma vez que {n} é um número inteiro menor que 0')
        else:
            for i in range(n, 1, -1):
                resposta *= i
        return f'{n}! = {resposta}'
    except UserWarning as e:
        return e
    except ValueError:
        return f'Impossível calcular, "{n}" não é um número inteiro'


if __name__ == '__main__':
    print(fatorial(input('Digite um número inteiro para calcular seu número fatorial: ')))
