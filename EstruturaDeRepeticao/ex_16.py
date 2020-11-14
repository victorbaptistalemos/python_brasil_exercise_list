"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500"""


def fibonacci(valor):
    valor = int(valor)
    numero_anterior = 0
    numero_posterior = 1
    print(numero_anterior)
    while numero_anterior <= valor:
        numero_posterior += numero_anterior
        numero_anterior *= -1
        numero_anterior += numero_posterior
        print(numero_anterior)


if __name__ == '__main__':
    fibonacci(500)
