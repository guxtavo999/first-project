
def minha_funcao(valor1, valor2):
    return valor1 + valor2

resposta = minha_funcao(10, 10)

print("reposta:", resposta)

def minha_func(valor3, valor4):
    return valor3 + valor4

while True:
    valor3 = int(input("Valor3: "))
    valor4 = int(input("Valor4: "))

    resposta = minha_func(valor3, valor4)
    print (valor3, "+", valor4, "=", resposta)