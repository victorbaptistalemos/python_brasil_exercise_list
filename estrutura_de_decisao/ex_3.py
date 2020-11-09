"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""


def seletor_de_sexo(sexo):
    """Retorna "Masculino", "Feminino" ou "Sexo Inválido".

    >>> print(seletor_de_sexo('m'))
    Masculino
    >>> print(seletor_de_sexo('F'))
    Feminino
    >>> print(seletor_de_sexo(''))
    Sexo Inválido


    :param sexo: string
    :return: string
    """

    sexo = ' ' if sexo == '' else str.upper(sexo[0])

    if sexo == 'M':
        return "Masculino"
    elif sexo == 'F':
        return "Feminino"
    else:
        return "Sexo Inválido"


if __name__ == '__main__':
    print(seletor_de_sexo(input("Digite o sexo [m/F]: ")))
