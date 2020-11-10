"""Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez."""


def calcular_media_escolar(nota_1, nota_2):
    """Calcula a média de duas notas escolares.
    Retorna uma mensagem de erro se a nota estiver fora da faixa.
    Retorna "Aprovado com Distinção" se a média for 10.0.
    Retorna "Aprovado" se a média for maior que 7.0 inclusive.
    Retorna "Reprovado" se a média for menor que 7.0 exclusive."""

    nota_1 = float(nota_1)
    nota_2 = float(nota_2)

    if not 0.0 <= nota_1 <= 10.0 or not 0.0 <= nota_2 <= 10.0:
        # se pelo menos uma das duas notas não estiver no intervalo de 0 a 10, será retornada uma string de erro
        return "A(s) nota(s) que você informou está(ão) inválida(s)."

    media = (nota_1 + nota_2) / 2

    if media < 7.0:
        return "Reprovado"
    elif 7.0 <= media < 10:
        return "Aprovado"
    else:
        return "Aprovado com Distinção"


if __name__ == '__main__':
    print(calcular_media_escolar(input("Digite a primeira nota: "), input("Digite a segunda nota: ")))
