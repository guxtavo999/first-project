import math
import os


x = 16
raiz_quad = math.sqrt(x) # função para descobrir raiz quadrada de algum número

print("A raiz quadrada de", x, "é igual a:", raiz_quad)

angulo = 45
seno = math.sin(angulo) # função para descobrir o seno de algum angulo
print("o seno de", angulo, "é igual a:", seno)

diretorio = os.getcwd() # função para gerar o diretório corrente, no caso o padrão que estamos trabalhando
print("O diretório corrente é: ", diretorio)

lista = [10, 20, 30]
tam = len(lista) # função para dar o tamanho de uma lista
print("A lista", lista, "tem tamanho", tam)

soma = sum(lista) # função para somar todos os elementos da lista
print("A lista", lista, "tem uma somatória igual a", soma)

# os.system("cls") /////////////////////////// (essa função é um clear, ela apaga o terminal inteiro)