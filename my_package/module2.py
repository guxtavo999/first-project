def products():
    produtos = []

    for _ in range(99999999):
        produto = {}
        produto["nome"] = input("Digite o nome do produto que deseja adicionar: ")
        produto["id"] = int(input("Digite o id desse produto: "))
        produto["preco"] = float(input("Digite o preço desse produto: "))
        produtos.append(produto)
        encerrar = input(f"Digite [C] para continuar e [P] para parar: ")
        if encerrar.upper() == "C":
            print("Adicionando mais um produto!")
            print()
        elif encerrar.upper() == "P":
            print("Encerrando o programa...")
            break
        for produto in produtos:
            print(f"nome do produto: {produto["nome"]}")
            print(f"id do produto: {produto["id"]}")
            print(f"preço do produto: {produto["preco"]}")
            print()

