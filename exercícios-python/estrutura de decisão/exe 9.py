#EXERCÍCIO: Faça um Programa que leia três números e mostre-os em ordem decrescente.

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if num_1 < num_3:
    num_1, num_3 = num_3, num_1
if num_1 < num_2:
    num_1, num_2 = num_2, num_1
if num_2 < num_3:
    num_2, num_3 = num_3, num_2        


print(f"Os números digitados em ordem descrescente são: {num_1}, {num_2}, {num_3}")

#COMENTÁRIO DA ALUNA (29/09/2023)
#pODEIA TER USADO UM LISTA? SIM, MAS O EXERCÍCIO É PARA USAR A CRIATIVIDADE PELOS IFS.
#ESTAVA MEU CÉREBRO BUGOU E ACHEI ESSA SOLUÇÃO LINDÍSSIMA NO STACK...: https://pt.stackoverflow.com/questions/460736/faça-um-programa-que-leia-três-números-e-mostre-os-em-ordem-decrescente-python
