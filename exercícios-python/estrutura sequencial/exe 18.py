#EXERCÍCIO 18:
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


tamanho_arquivo = int(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_link = int(input("Digite a velocidade do link (em Mbps):  "))

speed_seconds = tamanho_arquivo/(velocidade_link/8)

speed_minutes = speed_seconds/60

print(f"O tempo aproximado para download será de aproximadamente: {speed_minutes:.2f}")