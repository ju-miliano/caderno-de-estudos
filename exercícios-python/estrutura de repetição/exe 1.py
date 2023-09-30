#EXERCÍCIO 1: Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Dê uma nota de 0 a 10: "))

while nota >= 0 and nota <= 10:
    if nota>= 0 and nota <= 10:
        break
else:
    print("Valor inválido")    