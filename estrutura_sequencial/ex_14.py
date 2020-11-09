"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""


def calcular_multa(s):
    """Informa a quantidade de kg excedente e a multa a ser paga

    >>> calcular_multa(49)
    Não há excedente de peso.
    Não há multa a ser paga.
    >>> calcular_multa(55)
    Quantidade de quilos excedente: 5.0
    Valor da multa a ser paga: R$ 20.0

    :param s: string
    """

    excesso = 0.0 if s == '' or float(s) < 50.0 else float(s) - 50.0
    multa = 4.0 * excesso

    if excesso == 0.0:
        print('Não há excedente de peso.')
        print('Não há multa a ser paga.')
    else:
        print(f'Quantidade de quilos excedente: {excesso}')
        print(f'Valor da multa a ser paga: R$ {multa}')


if __name__ == '__main__':
    calcular_multa(input("Informe a pesagem de peixes em quilogramas: "))
