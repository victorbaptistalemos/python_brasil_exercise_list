"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo"""


def fibonacci(n_termo):
    n_termo = int(n_termo)
    numero_anterior = 0
    numero_posterior = 1
    termo = 1
    while termo <= n_termo:
        termo += 1
        numero_posterior += numero_anterior
        numero_anterior *= -1
        numero_anterior += numero_posterior
        print(numero_anterior)


if __name__ == '__main__':
    fibonacci(input('Insira a quantidade de termos fibonacci a ser impresso: '))
