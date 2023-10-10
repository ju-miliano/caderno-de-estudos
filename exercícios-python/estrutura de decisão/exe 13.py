#EXERCÍCIO 3: Faça um Programa que leia um número e exiba o dia correspondente da semana. 
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

entrada = int(input("Digite um número de 1 a 7: "))

if entrada == 1:
    print("1 - Domingo")
elif entrada == 2:
    print("2 - Segunda-Feira")
elif entrada == 3:
    print("3 - Terça-Feira")
elif entrada == 4: 
    print("4 - Quarta-Feira")
elif entrada == 5:
    print("5 - Quinta-Feira")
elif entrada == 6:
    print("6 - Sexta-Feira")
elif entrada == 7:
    print("7 - Sábado")         
else:
    print("Valor inválido.")                    

