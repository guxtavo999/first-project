class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fala(self):
        return f"{self.nome} é um(a) {self.especie}"


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro")
        self.raca = raca

    def fala(self):
        return f"{super().fala()} e late"


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, "Gato")
        self.cor = cor

    def fala(self):
        return f"{super().fala()} e mia"


dog = Cachorro('bilu', 'caramelo')
cat = Gato("Pipoca", "Rajado")

print("Atributos do cachorro:")
print(f"Nome: {dog.nome}")
print(f"Raça: {dog.raca}")
print(f"Espécie: {dog.especie}")
print()
print(dog.fala())
print()
print()

print("Atributos do Gato:")
print(f"Nome: {cat.nome}")
print(f"Cor: {cat.cor}")
print(f"Espécie: {cat.especie}")
print()
print(cat.fala())
