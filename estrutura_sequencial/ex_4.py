def media(*args):
    valor = 0
    contador = 0

    for valores in args:
        valor += 0 if valores == '' else int(valores)
        contador += 1

    return 0 if contador == 0 else valor / contador


primeira = input("Digite a primeira nota: ")
segunda = input("Digite a segunda nota: ")
terceira = input("Digite a terceira nota: ")
quarta = input("Digite a quarta nota: ")

print(media(primeira, segunda, terceira, quarta))
