persons = []

for _ in range(3):
    pessoa = {}
    pessoa["nome"] = input("Digite seu nome: ")
    pessoa["peso"] = float(input("Digite seu peso: "))
    pessoa["idade"] = int(input("Digite sua idade: "))
    persons.append(pessoa)

print("Dados das pessoas: ")
for pessoa in persons:
    print()
    print(f"Nome: {pessoa["nome"]}")
    print(f"Peso: {pessoa["peso"]}")
    print(f"Idade: {pessoa["idade"]}")
