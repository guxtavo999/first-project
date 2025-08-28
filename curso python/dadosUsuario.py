'''
idade = 0
altura = 0.0
nome = ""

idade = int(input("informe sua idade: "))
altura = float(input("Digite sua altura: "))
nome = str(input("Digite seu nome: "))

print("Parece que sua idade é", idade, ", sua altura é de", altura, "e seu nome é", nome)
'''

cpf = int(input("Digite seu cpf: "))
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
brasileiro = bool(input("Você é brasileiro? [Digite se for caso contrário apenas tecle Enter] ")) # quando o usuário digita alguma coisa no campo automaticamente bool vira True, quando ele não digita nada e deixa o campo em branco o bool automaticamente vira False

print(f"Seu cpf é:{cpf: d} \nseu nome é: {nome} \nseu salário é de: {salario} \ne você é brasileiro: {brasileiro}")
