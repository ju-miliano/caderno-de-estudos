#Exercício 17:
#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

cobertura_tinta = 6
capacidade_lata = 18
preco_lata = 80.0
capacidade_galoes = 3.6
preco_galao = 25.0

tamanho_area = float(input("Digite em metros quadrados (m²) o valor em da área a ser pintada:"))

litros = tamanho_area/cobertura_tinta

#latas inteiras
quantidade_latas = math.ceil (litros/capacidade_lata)
custo_latas = quantidade_latas*preco_lata
print (f""" 
    ------------------ Somente latas de 18L:
       Você precisa comprar {quantidade_latas} latas, que custarão R${custo_latas}
""")

#galões
quantidade_galoes = math.ceil (litros/capacidade_galoes)
custo_galoes = quantidade_galoes*preco_galao
print (f""" 
    ------------------ Somente galões de 3,6L:
       Você precisa comprar {quantidade_galoes} galões, que custarão R${custo_galoes}
""")

#mix
litros_necessarios_folgas = litros*1.1
quantidade_latas_mix = litros_necessarios_folgas//capacidade_lata

litros_necessarios_folgas_faltando = litros_necessarios_folgas - (quantidade_latas_mix*capacidade_lata)
quantidade_galoes_mix = math.ceil(litros_necessarios_folgas_faltando/capacidade_galoes)

custo_mix = (quantidade_latas_mix*preco_lata) + (quantidade_galoes_mix*preco_galao)
print (f""" 
    ------------------ Mix de latas e galões:
       Você precisa comprar {quantidade_latas_mix} latas e {quantidade_galoes_mix} galões, que custarão R${custo_mix}
""")

#Meu comentário: Buguei muito. A ajuda veio do post: https://cursos.alura.com.br/forum/topico-exercicio-python-iniciante-207085