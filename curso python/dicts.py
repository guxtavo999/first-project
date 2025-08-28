person = {
    "nome": "Teste",
    "peso": 0.0,
    "idade": 0
}

print(f"Dados da pessoa: {person}")
print(f"Nome: {person["nome"]}")
print(f"Peso: {person["peso"]}")
print(f"Idade: {person["idade"]}")
print()

person["nome"] = "Texto"
person["peso"] = 99.99
person["idade"] = 10

print(f"Dados da pessoa: {person}")
print(f"Nome: {person["nome"]}")
print(f"Peso: {person["peso"]}")
print(f"Idade: {person["idade"]}")
print()

person["nome"] = str(input("Digite seu nome: "))
person["peso"] = float(input("Digite seu peso: "))
person["idade"] = int(input("Digite sua idade: "))

print(f"Dados da pessoa: {person}")
print(f"Nome: {person["nome"]}")
print(f"Peso: {person["peso"]}")
print(f"Idade: {person["idade"]}")
print()

