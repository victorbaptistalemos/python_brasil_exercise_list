"""Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

    Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00"""


def folha_de_pagamento(valor_hora, total_hora):
    """Descreve um contracheque"""

    salario_bruto = float(valor_hora) * float(total_hora)
    _IR = {2500.0: 20, 1500.0: 10, 900.0: 5}
    _IRRF = 0
    _INSS = 10
    _FGTS = 11
    _SIND = 3

    for irrf in _IR:
        if salario_bruto > irrf:
            _IRRF = _IR[irrf]
            break

    irrf = _IRRF * salario_bruto / 100
    inss = _INSS * salario_bruto / 100
    fgts = _FGTS * salario_bruto / 100
    sindicato = _SIND * salario_bruto / 100

    print(f'Salário Bruto: ({valor_hora} * {total_hora})\t\t: R$ {salario_bruto:>7.2f}')
    print(f'(-) IR ({_IRRF} %):\t\t\t\t\t: R$ {irrf:>7.2f}')
    print(f'(-) INSS ({_INSS} %):\t\t\t\t: R$ {inss:>7.2f}')
    print(f'(-) SIND ({_SIND} %):\t\t\t\t\t: R$ {sindicato:>7.2f}')
    print(f'FGTS ({_FGTS} %):\t\t\t\t\t: R$ {fgts:>7.2f}')
    print(f'Salário Líquido: \t\t\t\t: R$ {salario_bruto - irrf - inss - sindicato:>7.2f}')


if __name__ == '__main__':
    folha_de_pagamento(input("Digite o valor da hora trabalhada: "),
                       input("Digite a quantidade de horas trabalhadas: "))
