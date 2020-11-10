"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste
    segundo o seguinte critério, baseado no salário atual:
        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5%
    Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento."""


def aumento_salarial(valor):
    """Detalha o valor do aumento salarial

    >>> aumento_salarial(250)
    Salário antigo: R$ 250.0
    Percentual de ajuste aplicado: 20.0%
    Valor do aumento salarial: R$ 50.0
    Novo salário: R$ 300.0
    >>> aumento_salarial(500)
    Salário antigo: R$ 500.0
    Percentual de ajuste aplicado: 15.0%
    Valor do aumento salarial: R$ 75.0
    Novo salário: R$ 575.0
    >>> aumento_salarial(750)
    Salário antigo: R$ 750.0
    Percentual de ajuste aplicado: 10.0%
    Valor do aumento salarial: R$ 75.0
    Novo salário: R$ 825.0000000000001

    :param valor:
    :return:
    """
    valor = float(valor)
    print(f'Salário antigo: R$ {valor}')

    if valor <= 280.0:
        ajuste = .2
    elif 280.0 < valor <= 700.0:
        ajuste = .15
    elif 700 < valor <= 1_500.0:
        ajuste = .1
    else:
        ajuste = .05

    print(f'Percentual de ajuste aplicado: {ajuste * 100}%')
    print(f'Valor do aumento salarial: R$ {valor * ajuste}')
    print(f'Novo salário: R$ {valor * (1 + ajuste)}')


if __name__ == '__main__':
    aumento_salarial(input("Digite o valor do salário atual: "))
