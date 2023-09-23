#EXERCÍCIO 3: Faça um Programa que verifique se uma letra digitada é "F", "M", "NB", "PNR", Outro (Qual?). 
#Conforme a letra escrever: F - Feminino, M - Masculino, NB - Não Binário, PNR - Prefiro não responder, 
#Comentário da aluna: Reformulei a pergunta para adequar-se a época em que estamos.

genero = input(f"""Digite a sigla como você se identifica:
               Opções:
               F - Feminino
               M - Masculino
               NB - Não binário
               Outro (Digite qual)
               """)

if genero == "F":
    print("Feminino")

elif genero == "M":
    print("Masculino")

elif genero == "NB":
    print("Não binário")

elif genero == "O":
    print(genero)

#Sei que ainda falta melhorar a estrutura, mas espero que possa atender a todos.