"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada."""


def tabuada(valor):
    valor = int(valor)
    print(f'Tabuada de {valor}:')
    for i in range(1, 11):
        print(f'{valor} X {i:>2} = {valor * i:>3}')


if __name__ == '__main__':
    tabuada(input('Informe o valor da tabuada: '))
