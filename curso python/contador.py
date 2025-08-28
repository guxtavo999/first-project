c = 0

while c < 99999999999:
    print("CONTADOR! NÚMERO ATUAL:", c)
    x = input("Digite 1 para incrementar o contador e 2 para decrementar, 3 caso queira encerrar o programa: ")
    if int(x) == 1:
        c = c + 1
    elif int(x) == 2:
        c = c - 1
    elif int(x) == 3:
        print("Encerrando o programa...")
        break
    else:
        print("Número inválido, tente novamente!")


contador = 0

for run in range(9999999):
    i = input("Digite se deseja continuar (s/n): ")
    if i == "n" or i == "N":
        break
    elif i =="s" or i=="S":
        contador += 1
        continue

print(f"Contador: {contador} ")