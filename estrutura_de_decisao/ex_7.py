"""Faça um Programa que leia três números e mostre o maior e o menor deles."""


def maior_e_menor_numero(*args):
    """Retorna o maior número a partir de uma lista de números."""

    maior_numero = float(args[0])
    menor_numero = float(args[0])

    for numero in args[1:]:
        if float(numero) > maior_numero:
            maior_numero = float(numero)
        else:
            menor_numero = float(numero)

    return f'O maior número é {maior_numero} e o menor é {menor_numero}'


if __name__ == '__main__':
    print(maior_e_menor_numero(input("Primeiro número: "), input("Segundo número: "), input("Terceiro número: ")))
