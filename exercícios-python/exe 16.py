#Exercício 16: Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

cobertura_tinta = 3
capacidade_lata = 18
preco_lata = 80.0

tamanho_area = float(input("Digite em metros quadrados o valor em m³ da área a ser pintada:"))

litros = tamanho_area/cobertura_tinta
latas_inteiras = int(litros/capacidade_lata)
if (litros%capacidade_lata != 0):
    latas_inteiras += 1

valor_total = latas_inteiras*preco_lata    

print(f"""Você precisará de {latas_inteiras} latas de tinta.
         O preço total é de R$ {valor_total}    
      """)

#Quero adicionar aqui que o Canal do Grabriel Souto foi o responsável por eu finalizar essa lógica que incluía
#as latas de tintas inteiras, que era o que me bugava no resultado final.
