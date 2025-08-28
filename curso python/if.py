nota = float(input("Digite a sua nota: "))

if float(nota) >= 7.0:
    print("Parabéns, você foi aprovado!")
elif float(nota <= 6.9) and float(nota >= 4.0):
    print("Você tem direito a fazer o exame!")
else:
    print("Que pena, você foi negado..")