from my_package.module1 import somar
from my_package.module1 import subtrair
from my_package.module1 import dividir

while True:
    print("Calculadora Simples - Digite uma opção a seguir:\n")
    calc = input("1 - Somar\n2 - Subtrair\n3 - Dividir\n")
    print()
    if calc == "1":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        res = somar(a, b)
        print(f"O resultado da soma entre {a} e {b} é: {res:.2f}")
    elif calc == "2":
        c = float(input("Digite o primeiro número: "))
        d = float(input("Digite o segundo número: "))
        res1 = subtrair(c, d)
        print(f"O resultado da subtração entre {c} e {d} é: {res1:.2f}")
    elif calc == "3":
        e = float(input("Digite o primeiro número: "))
        f = float(input("Digite o segundo número: "))
        res2 = dividir(e, f)
        print(f"O resultado da divisão entre {e} e {f} é: {res2:.2f}")
    else:
        print("Opção inválida!")
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() == "n":
        print("Encerrando a calculadora. Até mais!")
        break
    elif continuar.lower() == "s":
        continue   
    else:
        print("Opção inválida! Encerrando a calculadora.")
        break
