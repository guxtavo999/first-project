x = 5

y = id(x)

print(f"{x}, id de {x}: {y}")

x = 10

y = id(x)

print(f"{x}, id de {x}: {y}")

lista = [10, 20, 30]

print(f"Lista: {lista} ID da lista:  {id(lista)}")
lista.append(40)
lista[0] = 0
print(f"Lista: {lista} ID da lista:  {id(lista)}")
