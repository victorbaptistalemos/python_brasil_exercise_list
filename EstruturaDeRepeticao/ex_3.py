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
                raise UserWarning(f'O nome "{nome}" é muito curto, tente novamente')
        except UserWarning as e:
            nome = ''
            print(e)

    idade = -1
    while not 0 <= idade <= 150:
        idade = input('Digite a sua idade: ')
        try:
            idade = int(idade)
            if not 0 <= idade <= 150:
                raise UserWarning(f'A idade {idade} não é válida, digite entre 0 e 150, tente novamente')
        except UserWarning as e:
            print(e)
        except ValueError:
            print(f'O valor {idade} é inválido, a idade deve ser um número inteiro entre 0 e 150, tente novamente')
            idade = -1

    salario = 0
    while not salario > 0:
        salario = input('Digite o valor do salário: ')
        try:
            salario = round(float(salario), 2)
            if not salario > 0:
                raise UserWarning(f'O salário deve ser maior que 0, você digitou {salario}, tente novamente')
        except ValueError:
            salario = 0
            print('Você digitou um valor de salário inválido, tente novamente')
        except UserWarning as e:
            print(e)

    sexo = ''
    tupla_sexo = ('f', 'm')
    print('Informe seu sexo: [f = Feminino][m = Masculino]')
    while sexo == '':
        sexo = str.lower(input('[f/m]: '))
        try:
            tupla_sexo.index(sexo)
        except ValueError:
            sexo = ''
            print('Erro de digitação, tente novamente')

    estado_civil = ''
    tupla_estado_civil = ('c', 'd', 's', 'v')
    print('Informe seu estado civil: [c = Casado][d = Divorciado][s = Solteiro][v = Viúvo]')
    while estado_civil == '':
        estado_civil = str.lower(input('[c/d/s/v]: '))
        try:
            tupla_estado_civil.index(estado_civil)
        except ValueError:
            estado_civil = ''
            print('Erro de digitação, tente novamente')


if __name__ == '__main__':
    cadastro()
