"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações."""


def credenciais():
    usuario = ''
    senha = ''

    while usuario == senha:
        try:
            while usuario == '':
                usuario = input('Digite o nome do usuário: ')
            while senha == '':
                senha = input('Digite a senha: ')
            if usuario == senha:
                raise UserWarning('Os nomes de usuário e senha são iguais, tente novamente')
        except UserWarning as e:
            usuario = ''
            senha = ''
            print(e)


if __name__ == '__main__':
    credenciais()
