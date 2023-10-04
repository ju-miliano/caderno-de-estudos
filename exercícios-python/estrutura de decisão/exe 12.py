#EXERCÍCIOS 12: 
#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
#que depende do salário bruto (conforme tabela abaixo) 
#e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00


def hi():
    print(" Olá, vamos calcular o salário do funcionário.")

hi()

valor_hora = float(input("Digite o valor da hora trabalhada desse funcionário: "))
horas_trabalhadas = int(input("Digite o total de horas trabalhadas esse mês:"))

salario_bruto = valor_hora*horas_trabalhadas

#Salário Bruto até 900 (inclusive) - isento
if salario_bruto <= 900:
    # total do imposto de renda 
    imposto = 0
    #Desconto de 3% do sindicato     
    sindicato = ((3/100)*salario_bruto)
    #Cálculo fgts
    fgts_total = ((11/100)*salario_bruto)
    #soma dos descontos
    descontos_total = imposto+sindicato
    #salário líquido
    salario_liquido = salario_bruto-descontos_total
    
#Salário Bruto até 1500 (inclusive) - desconto de 5%
if salario_bruto <= 1500:
    # total do imposto de renda 
    imposto = ((5/100)*salario_bruto)
    #Desconto de 3% do sindicato     
    sindicato = ((3/100)*salario_bruto)
    #Cálculo fgts
    fgts_total = ((11/100)*salario_bruto)
    #soma dos descontos
    descontos_total = imposto+sindicato
    #salário líquido
    salario_liquido = salario_bruto-descontos_total

#Salário Bruto até 2500 (inclusive) - desconto de 10%
if salario_bruto <= 2500:
    # total do imposto de renda 
    imposto = ((10/100)*salario_bruto)
    #Desconto de 3% do sindicato     
    sindicato = ((3/100)*salario_bruto)
    #Cálculo fgts
    fgts_total = ((11/100)*salario_bruto)
    #soma dos descontos
    descontos_total = imposto+sindicato
    #salário líquido
    salario_liquido = salario_bruto-descontos_total

#Salário Bruto acima de 2500 - desconto de 20%
if salario_bruto > 2500:
    # total do imposto de renda 
    imposto = ((20/100)*salario_bruto)
    #Desconto de 3% do sindicato     
    sindicato = ((3/100)*salario_bruto)
    #Cálculo fgts
    fgts_total = ((11/100)*salario_bruto)
    #soma dos descontos
    descontos_total = imposto+sindicato
    #salário líquido
    salario_liquido = salario_bruto-descontos_total
    

print (f"""
    Salário Bruto:                  : R$ {salario_bruto}
    (-) IR (5%)                     : R$  {imposto}  
    (-) Sindicato ( 3%)             : R$  {sindicato}
    FGTS (11%)                      : R$  {fgts_total}
    Total de descontos              : R$  {descontos_total}
    Salário Liquido                 : R$  {salario_liquido}
    """)

#(03/10/2023) - Podem aparecer outros assuntos como fstring e funções, durante esses exercícios simples vou testando que aprendo por aí.