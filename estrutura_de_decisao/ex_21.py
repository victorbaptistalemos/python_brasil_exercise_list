"""Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina."""


def valor_levantamento():
    try:
        return int(input('Informe o valor para levantamento: '))
    except ValueError:
        return None


def caixa_eletronico():
    valor = valor_levantamento()
    if valor is None:
        print('Você digitou um valor inválido')
        return
    elif not 10 <= valor <= 600:
        print('O valor para levantamento digitado está fora da faixa permitida')
        return

    nota_de_100 = valor // 100
    nota_de_50 = valor % 100 // 50
    nota_de_10 = valor % 50 // 10
    nota_de_5 = valor % 10 // 5
    nota_de_1 = valor % 5

    print('Você irá levantar:', end=' ')
    if nota_de_100 > 0:
        print(f'{nota_de_100} nota(s) de R$ 100.00', end='')
        if nota_de_50 > 0 or nota_de_10 > 0 or nota_de_5 > 0 or nota_de_1 > 0:
            print(', ', end='')
    if nota_de_50 > 0:
        print(f'{nota_de_50} nota(s) de R$ 50.00', end='')
        if nota_de_10 > 0 or nota_de_5 > 0 or nota_de_1 > 0:
            print(', ', end='')
    if nota_de_10 > 0:
        print(f'{nota_de_10} nota(s) de R$ 10.00', end='')
        if nota_de_5 > 0 or nota_de_1 > 0:
            print(', ', end='')
    if nota_de_5 > 0:
        print(f'{nota_de_5} nota(s) de R$ 5.00', end='')
        if nota_de_1 > 0:
            print(', ', end='')
    if nota_de_1 > 0:
        print(f'{nota_de_1} nota(s) de R$ 1.00', end='')
    print()


if __name__ == '__main__':
    caixa_eletronico()
