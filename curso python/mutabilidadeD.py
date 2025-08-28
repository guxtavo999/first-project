def mutabilidade(a, b):  # AQUI ESTAREMOS SE TRATANDO DE NÚMEROS IMUTÁVEIS DENTRO DESSA FUNÇÃO
    if a > b:
        return a
    else:
        return b


a1 = float(input("Digite o primeiro número: "))
a2 = float(input("Digite o segundo número: "))
print(f"Números: {a1}, {a2}")
# AO EXECUTAR ESSA FUNÇÃO, TEREMOS ESSE ID
print(f"ID dos números: {id(a1)}, {id(a2)}")
print()

a1 = 5.0
a2 = 9.0

print(f"Números: {a1}, {a2}")
# AGORA APÓS ALTERAR O CONTEÚDO DAS VARIÁVEIS E EXECUTARMOS NOVAMENTE, TEREMOS OUTRO ID, POIS O PYTHON DELETA A1 E A2 DA MEMÓRIA E CRIA NOVAMENTE A1 E A2 EM OUTRO ESPAÇO DA MEMÓRIA MAS COM O MESMO NOME
print(f"ID dos números: {id(a1)}, {id(a2)}")
print()


def mutab(lista):
    for elem in lista:
        # NO CASO DESSA LISTA É UM OBJETO MUTÁVEL, QUE O PYTHON NÃO DELETA AO MUDAR DE CONTEÚDO
        print(f"Número: {elem}, ID do número: {id(elem)}")


list = [1, 3, 4, 6, 2, 43]

mutab(list)
print(f"ID da lista: {id(list)}")  # PODEMOS VER O ID ATUAL DA LISTA

list.append(22)

mutab(list)
# AQUI O ID APÓS A MODIFICAÇÃO CONTINUA O MESMO, POIS É UM OBJETO MUTÁVEL, O PYTHON VAI APENAS ADICIONAR MAIS UM NÚMERO AO CONTEÚDO DESSE OBJETO MUTÁVEL (LISTA)
print(f"ID da lista: {id(list)}")
