#Exercício 15: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#- Salário bruto.
#- Quanto pagou ao INSS.
# - Quanto pagou ao sindicato.
# - O salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
#- INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido. 

valor_hora = float(input("Digite quanto você ganha por hora:"))
horas_trabalhadas = int(input("Digite o número de horas que você trabalha por mês: "))

salario_bruto = valor_hora*horas_trabalhadas
imposto_de_renda = (salario_bruto*11)/100
inss = (salario_bruto*8)/100
sindicato = (salario_bruto*5)/100
salario_liquido = (salario_bruto)-(imposto_de_renda)-(inss)-(sindicato)

print(f"""
      + Salário Bruto: {salario_bruto}
      - IR: {imposto_de_renda}
      - INSS: {inss}
      - Sindicato: {sindicato}
      = Salário Liquido: {salario_liquido}
""")                        
