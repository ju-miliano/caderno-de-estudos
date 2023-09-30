#EXERCÍCIO 11: As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


salario1 = float(input("Digite seu salário atual: "))

if salario1 <= 280.00:
    salario2 = ((20/100)*salario1)+salario1
    aumento = "20%"
    valor_aumento = (20/100)*salario1

if salario1 > 280.00 and salario1 <= 700.00:
    salario2 = ((15/100)*salario1)+salario1
    aumento = "15%"
    valor_aumento = (15/100)*salario1

if salario1 > 700.00 and salario1 <= 1500.00:
    salario2 = ((10/100)*salario1)+salario1
    aumento = "10%"
    valor_aumento = (10/100)*salario1    

if salario1 > 1500.00:
    salario2 = ((5/100)*salario1)+salario1
    aumento = "5%"
    valor_aumento = (5/100)*salario1

print(f""" 
---------------------------------------------
 - Salário antes do reajuste: R$ {salario1}
 - Percentual do aumento aplicado: {aumento}
 - Valor do aumento: {valor_aumento}
 - Salário terá um aumento de: R$ {salario2} 
----------------------------------------------
""")
