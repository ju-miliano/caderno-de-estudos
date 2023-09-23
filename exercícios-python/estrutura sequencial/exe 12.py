#Exercício 12: Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite sua altura:  (Por exemplo: 1.64)"))

peso_ideal = (72.7*altura) - 58

print(f"Seu peso ideal é {peso_ideal:.2f}")

#Usei o f-string da aula de formatar strings da DIO para que o valor final apresentasse apenas 2 algorismos depois
# do ponto.