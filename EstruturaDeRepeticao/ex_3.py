"""Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';"""


def cadastro():
    nome = ''
    while nome == '':
        try:
            nome = input('Digite o seu nome: ')
            if len(nome) <= 3:
                raise UserWarning
        except UserWarning:
            nome = ''
            print('O nome é muito curto, tente novamente')

    idade = -1
    while not 0 <= idade <= 150:
        try:
            idade = int(input('Digite a sua idade: '))
            if not 0 <= idade <= 150:
                raise UserWarning
        except ValueError:
            print('Você digitou uma idade inválida, tente novamente')
        except UserWarning:
            idade = -1
            print('Você digitou uma idade fora da faixa permitida [0-150], tente novamente')

    salario = 0
    while not salario > 0:
        salario = input('Digite o valor do salário: ')
        try:
            salario = int(salario)
        except ValueError:
            pass
        try:
            salario = float(salario)

            if not salario > 0:
                raise UserWarning
        except ValueError:
            salario = 0
            print('Você digitou um valor de salário inválido, tente novamente')
        except UserWarning:
            print('Você digitou um valor de salário fora da faixa permitida [Salário > 0], tente novamente')

    sexo = ''
    print('Informe seu sexo: [f = Feminino][m = Masculino]')
    while sexo != 'f' and sexo != 'm':
        try:
            sexo = str.lower(input('[f/m]: '))
            if sexo != 'f' and sexo != 'm':
                raise UserWarning
        except UserWarning:
            sexo = ''
            print('Erro de digitação, tente novamente')

    estado_civil = ''
    tupla_estado_civil = ('c', 'd', 's', 'v')
    print('Informe seu estado civil: [c = Casado][d = Divorciado][s = Solteiro][v = Viúvo]')
    while estado_civil == '':
        try:
            estado_civil = str.lower(input('[c/d/s/v]: '))
            if len(estado_civil) > 1:
                raise ValueError
            tupla_estado_civil.index(estado_civil)
        except ValueError:
            estado_civil = ''
            print('Erro de digitação, tente novamente')


if __name__ == '__main__':
    cadastro()
