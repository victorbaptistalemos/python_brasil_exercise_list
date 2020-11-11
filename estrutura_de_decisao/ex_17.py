"""Faça um Programa que peça um número correspondente a um determinado ano
e em seguida informe se este ano é ou não bissexto."""


def ano_bissexto(ano):
    try:
        resposta = 'é' if int(ano) % 4 == 0 else 'não é'
        print(f'O ano {ano} {resposta} um ano Bissexto')
    except ValueError:
        print('Não foi possível calcular com o valor informado')


if __name__ == '__main__':
    ano_bissexto(input("Digite um ano válido: "))
