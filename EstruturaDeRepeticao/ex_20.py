"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
e limitando o fatorial a números inteiros positivos e menores que 16."""


def fatorial(n):
    try:
        n = int(n)
        resposta = 1
        if n < 0:
            raise UserWarning(f'Não é possivel calcular {n}!, uma vez que {n} é um número inteiro menor que 0')
        elif n > 16:
            raise UserWarning(f'Não é possivel calcular {n}!, a faixa de cálculo permitida é entre 0 e 16')
        else:
            for i in range(n, 1, -1):
                resposta *= i
        print(f'{n}! = {resposta}')
    except UserWarning as e:
        print(e)
    except ValueError:
        print(f'Impossível calcular, "{n}" não é um número inteiro')


def fatorial_continuo():
    print('Digite um número inteiro entre 0 e 16 para calcular o número fatorial, pressione Enter para terminar')
    valor = -1
    while not valor == '':
        valor = input('Fatorial de : ')
        if valor == '':
            return
        else:
            fatorial(valor)


if __name__ == '__main__':
    fatorial_continuo()
