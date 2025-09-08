def numbers(a, b):
    if a > b:
        return a
    else:
        return b


a1 = float(input("Digite o primeiro número: "))
a2 = float(input("Digite o segundo número: "))
res = numbers(a1, a2)
print(f"O maior número é: {res}")
