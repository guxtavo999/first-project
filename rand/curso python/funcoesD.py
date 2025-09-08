def calcS(a, b):
    soma = a + b
    return soma


def calcSS(c, d):
    if c > d:
        sub = c - d
    else:
        sub = d - c
    return sub


def calcM(e, f):
    mult = e * f
    return mult


def calcD(g, j):
    if g > j:
        div = g / j
    else:
        div = j / g
    return div


print("Para realizar uma soma digite S")
print("Para realizar uma subtração digite SS")
print("Para realizar uma multiplicação digite M")
print("Para realizar uma divisão digite D")
escolha = input("Selecione a opção desejada: ")
if escolha == "S":
    a1 = float(input("Digite o primeiro número: "))
    a2 = float(input("Digite o segundo número: "))
    res = calcS(a1, a2)
    print(f"O resultado da soma entre {a1} e {a2} é: {res}")
elif escolha == "SS":
    a3 = float(input("Digite o primeiro número: "))
    a4 = float(input("Digite o segundo número: "))
    res1 = calcSS(a3, a4)
    print(f"O resultado da subtração entre {a3} e {a4} é: {res1}")
elif escolha == "M":
    a5 = float(input("Digite o primeiro número: "))
    a6 = float(input("Digite o segundo número: "))
    res2 = calcM(a5, a6)
    print(f"O resultado da multiplicação entre {a5} e {a6} é: {res2}")
elif escolha == "D":
    a7 = float(input("Digite o primeiro número: "))
    a8 = float(input("Digite o segundo número: "))
    res3 = calcD(a7, a8)
    print(f"O resultado da divisão entre {a7} e {a8} é: {res3}")
