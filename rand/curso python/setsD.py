names1 = {"Carlos", "Josiel", "Jandira", "Aline"}
names2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

inter = names1.intersection(names2)
difer = names1.difference(names2)
difer2 = names2.difference(names1)
uniao = names1.union(names2)

print(f"Pessoas presentes nos dois grupos: {inter}")
print(f"Pessoas presentes em apenas um grupo: {difer, difer2}")
print(f"Lista de todas as pessoas: {uniao}")
