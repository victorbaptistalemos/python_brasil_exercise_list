"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra:
    tipo e quantidade de carne,
    preço total,
    tipo de pagamento,
    valor do desconto e valor a pagar."""


def recolher_dados():
    carne = ''

    while carne != 'A' and carne != 'F' and carne != 'P':
        try:
            carne = str.upper(input('Informe o tipo de carne [A = Alcatra][F = File Duplo][P = Picanha]: '))
        except ValueError:
            pass

    quantidade = -1

    while not quantidade > 0:
        quantidade = input('Informe a quantidade a ser comprada: ')
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

    quantidade = round(quantidade, 3)
    cartao_tabajara = ''

    while cartao_tabajara != 's' and cartao_tabajara != 'n':
        try:
            cartao_tabajara = str.lower(input('A compra será feita com o Cartão Tabajara? [S/n]: '))
        except ValueError:
            pass

    cartao_tabajara = True if cartao_tabajara == 's' else False

    return carne, quantidade, cartao_tabajara


def compras():
    preco_1 = {'A': 5.9, 'F': 4.9, 'P': 6.9}
    preco_2 = {'A': 6.8, 'F': 5.8, 'P': 7.8}
    nome_carne = {'A': 'Alcatra', 'F': 'Filé Duplo', 'P': 'Picanha'}

    print('Hipermercado Tabajara\n')
    print('Confira nossa tabela de preços:')
    print(f'{"":16}{"Até 5 Kg":>14}{"":10}{"Acima de 5 Kg":>14}')
    print(f'{"Filé Duplo":<16}R$ {preco_1["F"]:.2f} por Kg{"":10}R$ {preco_2["F"]:.2f} por Kg')
    print(f'{"Alcatra":<16}R$ {preco_1["A"]:.2f} por Kg{"":10}R$ {preco_2["A"]:.2f} por Kg')
    print(f'{"Picanha":<16}R$ {preco_1["P"]:.2f} por Kg{"":10}R$ {preco_2["P"]:.2f} por Kg')
    print()

    carne, quantidade, cartao_tabajara = recolher_dados()
    preco_total = 0.0

    if quantidade > 5:
        preco_carne = preco_2[carne]
        preco_total += preco_carne
        preco_total *= quantidade
    else:
        preco_carne = preco_1[carne]
        preco_total += preco_carne
        preco_total *= quantidade

    preco_total = round(preco_total, 2)

    print('Hipermercado Tabajara\n')
    print(f'{nome_carne[carne]:<12}R$ {preco_carne:<5}*{quantidade:<7.3f}+ R$ {preco_total:>7.2f}')

    desconto = 0.0

    if cartao_tabajara:
        desconto = round(preco_total * 0.05, 2)
        print(f'Desconto Cartão Tabajara:\t- R$ {desconto:>7.2f}')

    print(f'O valor a ser pago é:\t\t= R$ {preco_total - desconto:>7.2f}')


if __name__ == '__main__':
    compras()
