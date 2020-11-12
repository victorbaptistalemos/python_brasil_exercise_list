"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal."""


def captura_numeros():
    numero_1 = input('Digite o primeiro valor: ')

    try:
        if int(numero_1):
            numero_1 = int(numero_1)
    except ValueError:
        pass
    try:
        if type(numero_1) is int:
            pass
        else:
            numero_1 = float(numero_1)
    except ValueError:
        return None, None

    numero_2 = input('Digite o segundo valor: ')

    try:
        if int(numero_2):
            numero_2 = int(numero_2)
    except ValueError:
        pass
    try:
        if type(numero_2) is int:
            pass
        else:
            numero_2 = float(numero_2)
    except ValueError:
        return None, None

    return numero_1, numero_2


def calculos_diversos():
    numero_1, numero_2 = captura_numeros()
    try:
        if numero_1 is None:
            raise UserWarning

        operacao = {'A': (numero_1 + numero_2),
                    'D': (numero_1 / numero_2),
                    'E': (numero_1 ** numero_2),
                    'M': (numero_1 * numero_2),
                    'Q': numero_1 // numero_2,
                    'R': (numero_1 % numero_2),
                    'S': (numero_1 - numero_2)}

        print('Operações permitidas:')
        print('A = adicionar')
        print('D = dividir')
        print('E = exponenciação')
        print('M = multiplicar')
        print('Q = quociente da divisão')
        print('R = resto da divisão')
        print('S = subtrair')

        resultado = operacao[str.upper(input('Digite uma operação: '))]
        if resultado % 1 == 0:
            resultado = round(resultado)

        if type(resultado) == float:
            print(f'Não é possível dizer se {resultado} é par ou ímpar')
        elif resultado % 2 == 0:
            print('Par')
        else:
            print('Ímpar')
        if resultado < 0:
            print('Negativo')
        else:
            print('Positivo')
        if type(resultado) == float:
            print('Decimal')
        else:
            print('Inteiro')

    except UserWarning:
        print('Houve um erro de digitação')
    except KeyError:
        print('Operação inválida')


if __name__ == '__main__':
    calculos_diversos()
