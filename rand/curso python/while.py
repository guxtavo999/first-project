
i = 1

while i <= 10:  # CONTADOR DE 1 ATE 10, O += PEGA O I E SOMA COM MAIS UM NO NUMERO ATUAL
    print(i, " ", end="")
    i += 1


j = 10

while j >= 1:  # CONTADOR DE 10 ATE 1, O -= PEGA O J E SUBTRAI 1 DO NÚMERO ATUAL
    print(j)
    j -= 1


num = int(input("Digite um número inteiro: "))
while num > 0:  # O PROGRAMA FOI FEITO PARA SE ENCERRAR SOMENTE QUANDO O NUM FOR 0, QUALQUER NÚMERO ACIMA DE 0 ELE ENTRARA EM UM LOOP PARA QUE O USUARIO CONTINUE DIGITANDO
    print(num)
    num = int(input("Digite um número inteiro: "))

if num == 0:  # CASO O NUM SEJA 0, ELE ENCERRA O PROGRAMA E DIZ ESSA MENSAGEM
    print("Encerrando o programa...")
