"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""


def maior_menor_soma():
    lista = gera_lista()
    lista.sort()
    if len(lista) > 0:
        menor = lista[0]
        maior = lista[len(lista) - 1]
        soma = 0
        for i in lista:
            soma += i

        print(f'Maior número da lista: {maior}')
        print(f'Menor número da lista: {menor}')
        print(f'Soma dos itens da lista: {soma}')
    else:
        print('Impossível calcular, lista vazia')


def gera_lista():
    lista = []
    valor = -1
    print('Digite um valor entre 0 e 1000 para inserir na lista, pressione Enter para terminar')
    while not valor == '':
        try:
            valor = input('Digite um número inteiro entre 0 e 1000: ')
            if valor == '':
                return lista
            valor = int(valor)
            if not 0 <= valor <= 1000:
                raise UserWarning(f'Não é possível incluir "{valor}" na lista, tente novamente')
            else:
                lista.append(valor)
        except UserWarning as e:
            print(e)
        except ValueError:
            print(f'"{valor}" não é um número inteiro e, portanto, não pode ser inserido na lista, tente novamente')


if __name__ == '__main__':
    maior_menor_soma()
