'''''
nome = input ("Digite seu nome: ")
idade = int (input ("Digite sua idade: "))
peso = float(input ("Digite seu peso: "))

print(type(nome))
print(type(idade))
print(type(peso))

# ///////////////////////

soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print ("soma", soma)
print ("multiplicacao", multiplicacao)
print ("divisao", divisao)
print ("potencia", potencia)

# ////////////////////////
'''''
notas = []

contador = 1 

while contador <= 5:
    cod_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [cod_aluno, nota]
    notas.append(resultado)

    contador = contador + 1

print (" Quantidade de notas", len(notas))