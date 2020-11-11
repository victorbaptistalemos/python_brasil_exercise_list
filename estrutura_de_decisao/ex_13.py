"""Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. """


def dia_da_semana(numero):
    # Forma proposta reduzida

    br_day_week = {'1': 'Domingo',
                   '2': 'Segunda-feira',
                   '3': 'Terça-feira',
                   '4': 'Quarta-feira',
                   '5': 'Quinta-feira',
                   '6': 'Sexta-feira',
                   '7': 'Sábado'}

    if numero in br_day_week:
        print(br_day_week[numero])
    else:
        print("Valor inválido")


if __name__ == '__main__':
    dia_da_semana(input("Digite número do dia da semana: "))
