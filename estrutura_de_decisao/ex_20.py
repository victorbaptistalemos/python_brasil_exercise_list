"""Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10."""


def receber_notas():
    try:
        nota_1 = float(input("Digite a primeira nota: "))
        if not 0 <= nota_1 <= 10.0:
            raise ValueError
        nota_2 = float(input("Digite a segunda nota: "))
        if not 0 <= nota_2 <= 10.0:
            raise ValueError
        nota_3 = float(input("Digite a terceira nota: "))
        if not 0 <= nota_3 <= 10.0:
            raise ValueError
        return nota_1, nota_2, nota_3
    except ValueError:
        return None, None, None


def calcular_media():
    nota_1, nota_2, nota_3 = receber_notas()

    if nota_1 is None:
        print('Aconteceu algum erro na digitação de notas, tente novamente!')
        return

    media = (nota_1 + nota_2 + nota_3) / 3

    if media == 10.0:
        print('Aprovado com distinção')
    elif 7.0 <= media < 10.0:
        print(f'Aprovado! Sua média foi {media:.3f}')
    else:
        print(f'Reprovado! Sua média foi {media:.3f}')


if __name__ == '__main__':
    calcular_media()
