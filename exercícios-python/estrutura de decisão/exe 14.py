#EXERCÍCIO 14: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média,
# o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

notaparcial1 = float(input("Digite a primeira nota parcial: "))
notaparcial2 = float(input("Digite a segunda nota parcial: "))

media = (notaparcial1+notaparcial2)/2

if media >= 9.0 and media <= 10.0:
    conceito = "A"
    status = "APROVADO"

elif media >= 7.5 and media < 9.0:
    conceito = "B"
    status = "APROVADO"

elif media >= 6.0 and media < 7.5:
    conceito = "C"
    status = "APROVADO"

elif media >= 4.0 and media < 6.0:
    conceito = "D"
    status = "REPROVADO"

elif media >=0 and media < 4.0:
    conceito = "E"
    status = "REPROVADO"


print(f"""
          - Nota 1: {notaparcial1}
          - Nota 2: {notaparcial2}
          - Média: {media}
          - Conceito:{conceito}
          - Status:{status}

"""
          )