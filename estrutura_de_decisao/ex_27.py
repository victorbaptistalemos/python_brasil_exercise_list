"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos
e a quantidade (em Kg) de maças adquiridas
e escreva o valor a ser pago pelo cliente."""


def morango_e_maca():
    morango = -1
    while not morango >= 0:
        morango = input('Informe a pesagem dos morangos: ')
        try:
            morango = float(morango)
        except ValueError:
            pass
        try:
            if type(morango) is float:
                continue
            morango = int(morango)
        except ValueError:
            pass

    maca = -1

    while not maca >= 0:
        maca = input('Informe a pesagem dos morangos: ')
        try:
            maca = float(maca)
        except ValueError:
            pass
        try:
            if type(maca) is float:
                continue
            maca = int(maca)
        except ValueError:
            pass

    return morango, maca


def calcuar_preco_e_desconto():
    preco_1 = {'maca': 1.8, 'morango': 2.5}
    preco_2 = {'maca': 1.5, 'morango': 2.2}

    print('Confira nossa tabela de preços:')
    print(f'{"":16}{"Até 5 Kg":>14}{"":10}{"Acima de 5 Kg":>14}')
    print(f'{"Morango":<16}R$ {preco_1["morango"]:.2f} por Kg{"":10}R$ {preco_2["morango"]:.2f} por Kg')
    print(f'{"Maçã":<16}R$ {preco_1["maca"]:.2f} por Kg{"":10}R$ {preco_2["maca"]:.2f} por Kg')
    print()

    morango, maca = morango_e_maca()

    if morango > 5:
        morango *= preco_2['morango']
    else:
        morango *= preco_1['morango']

    if maca > 5:
        maca *= preco_2['maca']
    else:
        maca *= preco_1['maca']

    valor = morango + maca

    if valor > 25.0:
        valor *= 0.9

    valor = round(valor, 2)

    print(f'\nO valor a ser pago é: R$ {valor:.2f}')


if __name__ == '__main__':
    calcuar_preco_e_desconto()
