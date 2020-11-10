"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""


def sinal_do_numero(numero):
    """Retorna "Positivo" ou "Negativo" de acordo com o valor dado."""

    numero = 0 if numero == '' else float(numero)
    return 'Negativo' if numero < 0 else 'Positivo'


if __name__ == '__main__':
    print(sinal_do_numero(input("Informe um número: ")))
