v = []
s = 0

for i in range(5):
    dado = int(input("Digite um número inteiro: "))
    v.append(dado)
    s += dado

media = s / 5

for elem in v:
    print(elem, end=" ")

print(f"Média dos elementos: {media}")
