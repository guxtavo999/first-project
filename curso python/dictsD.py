produtos = []

for _ in range(5):
    produto = {}
    produto["nome"] = input("Digite o nome do produto: ")
    produto["id"] = int(input("Digite o id do produto: "))
    produto["preco"] = float(input("Digite o preço do produto: "))
    produtos.append(produto)
    for produto in produtos:
        print(f"nome do produto: {produto["nome"]}")
        print(f"id do produto: {produto["id"]}")
        print(f"preço do produto: {produto["preco"]}")
        print()
