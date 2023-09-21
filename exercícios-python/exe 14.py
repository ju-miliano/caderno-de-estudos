#Exercício 14: João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o 
#rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido 
#pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peso_peixinhos = float(input("Digite o peso total dos peixes de hoje: "))

excesso_peso_peixes = peso_peixinhos-50.00

if peso_peixinhos <=50.00:
    multa_excesso = 0
    print("Não houve peso excedido, portanto não há multas a pagar.")
elif peso_peixinhos > 50.00:
    multa_excesso = excesso_peso_peixes*4.00
    print("O peso excedido foi de ", excesso_peso_peixes,"kg.", "E o total da multa é de R$", multa_excesso)


#DOC
#20/09/2023
#Confundi a lógica, mas deu tudo certo no final.