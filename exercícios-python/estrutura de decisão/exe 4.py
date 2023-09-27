#EXERCÍCIO4: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra do alfabeto: ")
vogais = "aeiou"

if letra in vogais or letra in vogais.upper():
    print ("A letra digitada é uma vogal.")
else:
    print ("A letra digitada é uma consoante.") 


#27/09/2023
#Demorei um pouco nesse exercício que parecia ser tão simples, mas passei um tempo procurando uma forma de aceitar
# as letras maiúsculas e minúsculas sem ter que colocar elif com cada vogal e letra.
#Um grande obrigada para o vídeo do Kenny no Youtube. (https://www.youtube.com/watch?v=lZGCvq2ZUAA)