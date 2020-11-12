"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que
    o preço do litro da gasolina é R$ 2,50
    o preço do litro do álcool é R$ 1,90."""


def quantidade_e_tipo():
    quantidade = 0
    while not quantidade > 0:
        quantidade = input('Informe a quantidade de litros a ser vendido: ')
        try:
            quantidade = float(quantidade)
        except ValueError:
            pass
        try:
            if type(quantidade) is float:
                continue
            quantidade = int(quantidade)
        except ValueError:
            pass
    tipo = ''
    while tipo != 'A' and tipo != 'G':
        try:
            tipo = str.upper(input('Informe o tipo de combustívela: [A = Álcool][G = Gasolina]: '))
        except ValueError:
            pass

    return quantidade, tipo


def desconto_combustivel():
    quantidade, tipo = quantidade_e_tipo()

    preco = {'A': 1.9, 'G': 2.5}
    desconto_1 = {'A': 0.03, 'G': 0.04}
    desconto_2 = {'A': 0.05, 'G': 0.06}

    valor = quantidade * preco[tipo]

    if quantidade > 20:
        valor *= 1 - desconto_2[tipo]
    else:
        valor *= 1 - desconto_1[tipo]

    print(f'O valor a ser pago é: {valor:.2f}')


if __name__ == '__main__':
    desconto_combustivel()
