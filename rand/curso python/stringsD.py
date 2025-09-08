palavras = []

while True:
    palavra = input("Digite uma palavra (ou '/exit' para sair): ")
    if palavra == "/exit":
        break
    palavras.append(palavra)
    resultado = " ".join(palavras)
    print("Palavras digitadas:", resultado)
