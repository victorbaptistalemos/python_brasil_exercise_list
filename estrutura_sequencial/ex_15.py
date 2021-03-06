"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:
    11% para o Imposto de Renda,
    8% para o INSS e
    5% para o sindicato.

Formato de resposta:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato (5%) : R$
    = Salário Liquido : R$"""


def calcular_salario(valor_hora, total_hora):
    """Calcula o salário com base no valor da hora e quantidade trabalhadas"""

    _IRRF = .11  # Imposto de Renda Retido na Fonte
    _INSS = .08  # Instituto Nacional do Seguro Social
    _Sindicato = .05  # Contribuição Sindical
    salario_bruto = float(valor_hora) * float(total_hora)
    imposto_renda = salario_bruto * _IRRF
    imposto_seguro_social = salario_bruto * _INSS
    contribuicao_sindical = salario_bruto * _Sindicato
    salario_liquido = salario_bruto - imposto_renda - imposto_seguro_social - contribuicao_sindical

    print(f'+ Salário Bruto : R$ {salario_bruto}')
    print(f'- IR (11%) : R$ {imposto_renda}')
    print(f'- INSS (8%) : R$ {imposto_seguro_social}')
    print(f'- Sindicato (5%) : R$ {contribuicao_sindical}')
    print(f'= Salário Liquido : R$ {salario_liquido}')


if __name__ == '__main__':
    calcular_salario(input("Informe o valor da hora trabalhada: "), input("Informe o total de horas trabalhadas: "))
