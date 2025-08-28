linhas = 3
colunas = 4

# Inicializando a matriz vazia
matriz = []

# Preenchendo a matriz com valores do usuário
print("Preencha a matriz 3x4:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para a posição ({i},{j}): "))
        linha.append(valor)
    matriz.append(linha)

# Inicializando variáveis para armazenar o maior e menor valores e suas posições
maior = matriz[0][0]
menor = matriz[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

# Encontrando o maior e menor elemento e suas posições
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos_maior = (i, j)
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_menor = (i, j)

# Exibindo a matriz e os resultados
print("\nMatriz preenchida:")
for linha in matriz:
    print(linha)

print(f"\nO maior elemento é {maior} e está na posição {pos_maior}.")
print(f"O menor elemento é {menor} e está na posição {pos_menor}.")
