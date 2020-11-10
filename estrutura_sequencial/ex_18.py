"""Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). """

from math import ceil as ceil


def tempo_download(tamanho, velocidade):
    """Calcula o tempo aproximado de download considerando:
    tamanho do arquivo,
    velocidade de conexão e
    transferência contínua, ou seja, não oscila."""


    print(f'Tempo estimado de download: {ceil(float(tamanho) / (float(velocidade) / 8) / 60)} minuto(s)')
    # Considerando que tanto faz tamanho*8/veloc/segundos como a forma retornada, o resultado é o mesmo.


if __name__ == '__main__':
    tempo_download(input('Digite o tamanho do arquivo (MB): '), input('Digite a velocidade de conexão (Mbps): '))
