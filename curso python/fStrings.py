print("Olá, seja bem-vindo!")

print("O valor inteiro é: ", 10)
print(f"O valor inteiro em decimal é: {10: d}") 
print(f"O valor inteiro em binário é: {10: b}")

print(f"O valor de Pi é: {3.14159265: f}")
print(f"O valor de Pi é: {3.14159265: .2f}")

nome = input("Digite seu nome: ")
nacionalidade = input("Digite sua nacionalidade: ")
salario = float(input("Digite seu salario: "))
print(f"Nome:\t\t{nome}\nNacionalidade:\t{nacionalidade}\nSalário:\tR$ {salario:.3f}") #usamos o \t para adicionar um espaço no texto e o \n para quebrar uma linha de espaço
