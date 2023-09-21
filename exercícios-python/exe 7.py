#Exercício 7: Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import math

lado_quadrado = float(input("Digite o valor de um dos lados do quadrado: "))
area_quadrado = math.pow(lado_quadrado,2)
dobro_area = area_quadrado*2
print("O dobro da área é: ",dobro_area)
