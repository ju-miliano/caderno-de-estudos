#Exercício 8:
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato.
produto1 = input("Qual o nome do primeiro produto que você deseja comprar? ")
preco1 = float(input("Digite o preço do primeiro produto: "))
produto2 = input("Qual o nome do segundo produto que você deseja comprar? ")
preco2 = float(input("Digite o preço do segundo produto: "))
produto3 = input("Qual o nome do terceiro produto que você deseja comprar? ")
preco3 = float(input("Digite o preço do terceiro produto: "))


menor_preco = preco1
compra = produto1

if (preco2 < menor_preco):
    menor_preco = preco2
    compra = produto2

if (preco3 < menor_preco):
    menor_preco = preco3
    compra = produto3


print(f"Você deve comprar o produto {compra}.")