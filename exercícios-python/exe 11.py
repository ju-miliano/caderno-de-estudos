#Exercício 10: Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.
import math
number_I = int(input("Digite um número inteiro: "))
number_II = int(input("Digite um número inteiro: "))
number_III = float(input("Digite um número inteiro: "))

Resultado_A = (number_I*2)*(number_II/2)
print ("Resulatdo A: ", Resultado_A)

Resultado_B = (number_I*3) + number_III
print ("Resulatdo B: ", Resultado_B)

Resultado_C = math.pow(number_III,3)
print ("Resulatdo C: ", Resultado_C)