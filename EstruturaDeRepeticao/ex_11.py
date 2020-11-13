"""Altere o programa anterior para mostrar no final a soma dos números"""


def imprimir_intervalo_e_soma(inicio, fim):
    soma = 0
    for i in range(inicio, fim + 1):
        print(i)
        soma += i
    print()
    print(soma)


if __name__ == '__main__':
    imprimir_intervalo_e_soma(1, 20)
