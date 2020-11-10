"""Faça um Programa que leia três números e mostre o maior e o menor deles."""


def maior_numero(*args):
    """Retorna o maior número a partir de uma lista de números."""

    numero_maior = float(args[0])

    for numero in args[1:]:
        if float(numero) > numero_maior:
            numero_maior = float(numero)

    return numero_maior


if __name__ == '__main__':
    print(maior_numero(input("Primeiro número: "), input("Segundo número: "), input("Terceiro número: ")))
