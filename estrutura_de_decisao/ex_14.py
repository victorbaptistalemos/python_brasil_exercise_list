"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E."""


def calcular_media(nota_1, nota_2):
    nota_1 = float(nota_1)
    nota_2 = float(nota_2)
    conceitos = {4.0: 'E', 6.0: 'D', 7.5: 'C', 9.0: 'B', 10.0: 'A'}

    media = (nota_1 + nota_2) / 2
    conceito = str

    for medias in conceitos:
        if media <= medias:
            conceito = conceitos[medias]
            break

    print(f'Primeira nota:\t{nota_1:>5.2f}')
    print(f'Segunda nota:\t{nota_2:>5.2f}')
    print(f'Conceito:\t\t{conceito}')

    if conceito == 'A' or 'B' or 'C':
        print('APROVADO')
    else:
        print('REPROVADO')


if __name__ == '__main__':
    calcular_media(input("Digite a primeira nota: "), input('Digite a segunda nota: '))
