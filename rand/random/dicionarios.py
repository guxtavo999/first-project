'''
Dicionarios usam chave e valor para armazenar informações 

variavel = {
    "chave": "valor",
}
'''

pessoa = {
    "nome": "Programador Python",
    "idade": 27,
    "peso": 73.3
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])

# informações do jogador
player ={
    "nome": "Gustavo",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5,
}

# lista de inimigos
npcs = [
    {"nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    {"nome": "Monstro", "dano": 10, "hp": 110, "exp": 10},
    {"nome": "Monstrão", "dano": 15, "hp": 120, "exp": 12},
    {"nome": "Chefão", "dano": 40, "hp": 190, "exp": 40}
]

print (player)
print (npcs[1])
