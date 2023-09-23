#Exercício 9: Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

temperaturaF = float(input("Digite a temperatura em Fahrenheit: "))

temperatura_celcius = 5*((temperaturaF-32) / 9)

print("A temperatura em Celcius é igual a ", temperatura_celcius, " °C")