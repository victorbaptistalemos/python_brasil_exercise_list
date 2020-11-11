"""Faça um Programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros."""


def descricao_numerica(numero):
    try:
        numero = int(numero)
        if not 0 < numero < 1000:
            raise UserWarning

        centena = numero // 100
        is_centena = centena > 0
        dezena = numero % 100 // 10
        is_dezena = dezena > 0
        unidade = numero % 10
        is_unidade = unidade > 0

        if centena > 1:
            print(f'{centena} centenas', end='')
        elif centena == 1:
            print(f'{centena} centena', end='')
        if is_centena and is_dezena and is_unidade:
            print(', ', end='')
        elif is_centena and is_dezena:
            print(' e ', end='')
        if dezena > 1:
            print(f'{dezena} dezenas', end='')
        elif dezena == 1:
            print(f'{dezena} dezena', end='')
        if is_unidade:
            print(' e ', end='')
        if unidade > 1:
            print(f'{unidade} unidades')
        elif unidade == 1:
            print(f'{unidade} unidade')
    except ValueError:
        print('O valor digitado não é um número')
    except UserWarning:
        print('O valor digitado está fora da faixa de cálculo')


if __name__ == '__main__':
    descricao_numerica(input('Digite um valor positivo não nulo menor que 1000: '))
