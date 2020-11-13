"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação."""


def calculo_de_crescimento(populacao_a, taxa_a, populacao_b, taxa_b):
    anos = 0

    if populacao_a == populacao_b:
        return anos
    elif populacao_a > populacao_b:
        if taxa_a > taxa_b:
            return anos
        while populacao_a > populacao_b:
            populacao_a *= taxa_a / 100 + 1
            populacao_b *= taxa_b / 100 + 1
            anos += 1
    else:
        if taxa_a < taxa_b:
            return anos
        while populacao_a < populacao_b:
            populacao_a *= taxa_a / 100 + 1
            populacao_b *= taxa_b / 100 + 1
            anos += 1

    return anos


def recolher_dados():
    populacao_a = -1
    populacao_b = -1
    taxa_a = -1.0
    taxa_b = -1.0

    while not populacao_a > 0 or not taxa_a > 0 or not populacao_b > 0 or not taxa_b > 0:
        try:
            if not populacao_a > 0:
                populacao_a = input('Insira a quantidade de pessoas da primeira população: ')
                populacao_a = int(populacao_a)
                if not populacao_a > 0:
                    raise UserWarning(f'O valor {populacao_a} não é válido, digite um número inteiro > 0')
            if not taxa_a > 0:
                taxa_a = input('Insira a taxa de crescimento da primeira população (1.05% => 1.05): ')
                taxa_a = float(taxa_a)
                if not taxa_a > 0:
                    raise UserWarning(f'O valor {taxa_a} não é válido, digite um número > 0')
            if not populacao_b > 0:
                populacao_b = input('Insira a quantidade de pessoas da segunda população: ')
                populacao_b = int(populacao_b)
                if not populacao_b > 0:
                    raise UserWarning(f'O valor {populacao_b} não é válido, digite um número inteiro > 0')
            if not taxa_b > 0:
                taxa_b = input('Insira a taxa de crescimento da segunda população (1.05% => 1.05): ')
                taxa_b = float(taxa_b)
                if not taxa_b > 0:
                    raise UserWarning(f'O valor {taxa_b} não é válido, digite um número > 0')
        except UserWarning as e:
            print(e)
        except ValueError:
            if not isinstance(populacao_a, int):
                print(f'O valor "{populacao_a}" é inválido, digite um número inteiro > 0, tente novamente')
                populacao_a = -1
            if not isinstance(populacao_b, int):
                print(f'O valor "{populacao_b}" é inválido, digite um número inteiro > 0, tente novamente')
                populacao_b = -1
            if not isinstance(taxa_a, float):
                print(f'O valor "{taxa_a}" é inválido, digite um número > 0, tente novamente')
                taxa_a = -1.0
            if not isinstance(taxa_b, float):
                print(f'O valor "{taxa_b}" é inválido, digite um número > 0, tente novamente')
                taxa_b = -1.0

    return populacao_a, taxa_a, populacao_b, taxa_b


def tempo_de_crescimento():
    populacao_a, taxa_a, populacao_b, taxa_b = recolher_dados()

    tempo = calculo_de_crescimento(populacao_a, taxa_a, populacao_b, taxa_b)

    if tempo == 0:
        if populacao_a == populacao_b:
            print(f'As populações são iguais e ', end='')
            if taxa_a == taxa_b:
                print('não é possível calcular, uma vez que a taxa de crescimento são iguais')
            elif taxa_a > taxa_b:
                print('em 1 ano a primeira população ultrapassará a segunda população')
            else:
                print('em 1 ano a segunda população ultrapassará a primeira população')
        elif populacao_a > populacao_b:
            print('Não é possível calcular, ', end='')
            print('uma vez que a tanto a taxa de crescimento quanto o tamanho da primeira população ', end='')
            print('são maiores que os da segunda população')
        else:
            print('Não é possível calcular, ', end='')
            print('uma vez que a tanto a taxa de crescimento quanto o tamanho da segunda população ', end='')
            print('são maiores que os da primeira população')


if __name__ == '__main__':
    tempo_de_crescimento()
