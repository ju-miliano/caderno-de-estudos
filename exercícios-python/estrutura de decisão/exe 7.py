#Exercício 7: Faça um Programa que leia três números e mostre o maior e o menor deles.

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))

#Maior número:
maior = num_1

if num_2 > maior:
    maior = num_2
if num_3 > maior:
    maior = num_3

#menor número:
menor = num_1

if num_2 < menor:
    menor = num_2
if num_3 < menor:
    menor = num_3

print(f"""
      O maior número digitado é: {maior}
      O menor número digitado é: {menor}
      """)


#Comentário da aluna(29/09/2023):
#Fiquei confusa, então fui procurar no Google. Encontrei diversas respostas com 
#soluções diferentes, por isso escolhi adicionar aqui a que eu consegui entender.
#https://www.pythonprogressivo.net/2018/02/Recebe-Tres-Numeros-Exibe-Maior-Menor.html