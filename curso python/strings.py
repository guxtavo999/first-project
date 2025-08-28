nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

comp_nome = len(nome)
comp_sobrenome = len(sobrenome)

nome_completo = nome + " " + sobrenome
comp_nome_completo = len(nome_completo)

print(f"Comprimento do nome: {comp_nome}")
print(f"Comprimento do sobrenome: {comp_sobrenome}")

print(f"O nome completo é: {nome_completo}")
print(f"O comprimento do nome completo é: {comp_nome_completo}")
