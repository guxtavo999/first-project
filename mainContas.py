from my_package.module1 import somar
from my_package.module1 import subtrair
from my_package.module1 import dividir

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
res = somar(a, b)
print(f"O resultado da soma entre {a} e {b} é: {res:.2f}")


c = float(input("Digite o primeiro número: "))
d = float(input("Digite o segundo número: "))
res1 = subtrair(c, d)
print(f"O resultado da subtração entre {c} e {d} é: {res1:.2f}")


e = float(input("Digite o primeiro número: "))
f = float(input("Digite o segundo número: "))
res2 = dividir(e, f)
print(f"O resultado da divisão entre {e} e {f} é: {res2:.2f}")
