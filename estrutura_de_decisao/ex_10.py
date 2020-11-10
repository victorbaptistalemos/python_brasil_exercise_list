"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""


def qual_turno():
    print("Qual turno que você estuda?")
    turno = str.upper(input("Digite M para matutuno, V para vespertino ou N para noturno: "))

    turnos = {'M': 'Bom dia!', 'V': 'Boa Tarde!', 'N': 'Boa noite!'}

    # Aprimorando para try except (Foge ao proposto if elif else)
    try:
        print(turnos[turno])
    except KeyError:
        print('Valor Inválido!')


if __name__ == '__main__':
    qual_turno()
