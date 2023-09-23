#Exercício 4: Faça um Programa que peça as 4 notas bimestrais e mostre a média.

bimestre1 = float(input("Digite a nota do primeiro bimestre: "))
bimestre2 = float(input("Digite a nota do segundo bimestre: "))
bimestre3 = float(input("Digite a nota do terceiro bimestre: "))
bimestre4 = float(input("Digite a nota do quarto bimestre: "))

media = (bimestre1 + bimestre2 + bimestre3 + bimestre4)/4

print("A média bimestral é de  ", media)

#MUITO IMPORTANTE: DECIMAIS EM PYTHON SE COLOCA O PONTO E NÃO A VÍRGULA, CABEÇÃO