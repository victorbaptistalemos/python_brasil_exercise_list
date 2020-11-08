"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês."""


def salario_mes(valor_hora, total_hora):
    """Calcula o salário do mês com base no valor e hora dados

    >>> salario_mes(50, 100)
    5000.0
    >>> salario_mes(22.3, 220)
    4906.0

    :param valor_hora: string
    :param total_hora: string
    :return: float
    """

    return float(valor_hora) * float(total_hora)


if __name__ == '__main__':
    print(salario_mes(input("Digite o valor da hora trabalhada: "), input("Digite o total de horas trabalhadas: ")))
