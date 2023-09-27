#Exercício 6: Faça um Programa que leia três números e mostre o maior deles.

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))

if num_1 > num_2 and num_1 > num_3:
    print("O maior número digitado é: ", num_1) 
    
elif num_2 > num_1 and num_2 > num_3:
    print("O maior número digitado é: ", num_2) 

elif num_3 > num_1 and num_3 > num_2:
    print("O maior número digitado é: ", num_3) 
