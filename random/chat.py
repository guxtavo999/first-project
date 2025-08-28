import os   # usado para importar alguma coisa, no caso do os será o sistema operacional

mensagens = []

nome = input("Nome: ")

while True:                  #Sempre será verdadeiro

    # Limpando o terminal 
    os.system('cls') # usado para dar clear no terminal "cls = clear"

    if len(mensagens) > 0: # len acompanhado de lista = passa o tamanho da lista, ou seja se ela for maior que 0 vai rodar o código
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    
    print("_____________________")

    # obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break # quebra o loop para não ficar infinito e para de rodar o codigo

    # adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })