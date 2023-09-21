#Exercício 6: Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math
raio= float(input("Digite valor do raio do círculo: "))

pi = 3.1415
area = math.pow(raio,2)*pi

print("A área é igual a ", area)

