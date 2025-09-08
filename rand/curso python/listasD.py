l = []

for i in range(9999999):
    dado = int(input("Digite um número inteiro: "))
    l.append(dado)
    if dado == 0:
        print("Encerrando o programa...")
        break

m1 = min(numero for numero in l if numero !=0)
m2 = max(l)

print(f"Quantidade de elementos adicionados na lista: {len(l)}, Menor elemento da lista: {m1}, Maior elemento da lista: {m2}")