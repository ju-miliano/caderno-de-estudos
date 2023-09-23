#Exercício 13: Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

print(f"""
      Atenção, esse algoritmo não tem a intenção de ofender ou espalhar qualquer tipo de desinformação e ódio. 
      Sou apenas uma estudante fazendo uma lista de exercícios para inicante no Python.

      """)
altura = float(input("Digite sua altura como mostra o exemplo: 1.64:  "))
genero_bio = input("Como você indentifica seu gênero biológico? Responda M para Mulher e H para Homem.")

if genero_bio == "M":
    peso_ideal = (62.1*altura) - 44.7
    
else:
    peso_ideal = (72.7*altura) - 58

print(f"Seu peso ideal é {peso_ideal:.2f}")


#Doc
#Usei o f""" para formatar a string tripla/múltipla 
#Como no exercício 12, usei o f-string para delimitar o número de algarismos.