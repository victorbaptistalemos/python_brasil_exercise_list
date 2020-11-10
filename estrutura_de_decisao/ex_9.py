"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""


def lista_de_numeros():
    """Lê três números e os retorna em ordem decrescente."""

    lista = []

    for valores in range(3):
        lista.append(input("Insira um valor: "))

    lista.sort()
    lista.reverse()

    for valores in lista:
        print(valores)


if __name__ == '__main__':
    lista_de_numeros()
