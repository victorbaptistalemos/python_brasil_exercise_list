"""Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido."""


def recolher_nota():
    nota = -1

    while not 0 <= nota <= 10:
        nota = input('Informe a quantidade a ser comprada: ')
        try:
            nota = float(nota)
        except ValueError:
            pass
        try:
            if not type(nota) is float:
                nota = int(nota)
        except ValueError:
            print('Você não digitou um número')

        if type(nota) is str:
            nota = -1
        elif not 0 <= nota <= 10:
            print('A nota digitada não é válida')

    return nota


if __name__ == '__main__':
    recolher_nota()
