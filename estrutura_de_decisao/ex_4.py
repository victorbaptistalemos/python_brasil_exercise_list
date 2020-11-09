"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""


def vogal_ou_consoante():
    """ Retorna "Vogal" ou "Consoante"

    :return: string
    """

    teste = input("Digite uma letra: ")

    while teste == '' or teste[0].isdigit() or len(teste) > 1:
        if len(teste) > 1:
            teste = input("Só preciso de uma letra. Digite somente uma letra: ")
        else:
            teste = input("Você não digitou uma letra. Digite uma letra: ")

    return 'Vogal' if 'aeiou'.find(str.lower(teste[0])) != -1 else 'Consoante'


if __name__ == '__main__':
    print(vogal_ou_consoante())
