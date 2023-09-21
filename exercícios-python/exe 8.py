#Exercício 8: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Digite quanto você ganha por hora: "))
resposta_horastrabalhadas = input("Você sabe quantas horas você trabalha por mês? Digite S para sim e N se a reposta for não." )
if resposta_horastrabalhadas == 'S':
        horas_trabalhadas_mensal =  int(input("Digite quantas horas você trabalha por mês: "))
else: 
    horas_semanais = int(input("Quantas horas você trabalha por semana?"))
    horas_trabalhadas_mensal = horas_semanais*4

salario_mensal = valor_hora*horas_trabalhadas_mensal

print("O seu salário mensal será de:", salario_mensal)



#Ia me extender para expecificar diasxhoras caso a pessoa não soubesse o total de horas por mês, mas preciso finalizar pelo menos os 10 exercícios hoje.    