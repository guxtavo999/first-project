mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elementos da primeira linha: ")
for elem in mat[0]:
    print(elem, end=" ")

print()

print("Todos os elementos de mat: ")
for linha in mat:
    for elem in linha:
        print(elem, end=" ")
    print()

print(f"Penúltimo elemento da matriz: {mat[2][1]}")