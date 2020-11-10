"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""


def media(*args):
    """Retorna a média dos valores digitados"""

    valor = 0
    contador = 0

    for valores in args:
        valor += 0 if valores == '' else int(valores)
        contador += 1

    return 0 if contador == 0 else valor / contador


if __name__ == '__main__':
    primeira = input("Digite a primeira nota: ")
    segunda = input("Digite a segunda nota: ")
    terceira = input("Digite a terceira nota: ")
    quarta = input("Digite a quarta nota: ")

    print(media(primeira, segunda, terceira, quarta))
