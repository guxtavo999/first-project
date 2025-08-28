def cadClientes():

    def validar_cpf(cpf):
        cpf_limpo = cpf.replace(".", "").replace("-", "").strip()
        if len(cpf_limpo) == 11 and cpf_limpo.isdigit():
           return True
        return False

    def validar_telefone(tel):
        tel_limpo = tel.replace("(", "").replace(")", "").replace("-", "").replace(" ", "").strip()
        if tel_limpo.isdigit() and 10 <= len(tel_limpo) <= 11:
            return True
        return False

    print(">>>>> SISTEMA DE CADASTRO DE NOVOS CLIENTES <<<<<")
    clientes = []

    while True:
        cliente = {}
        while True:
            nome = input("Digite o nome do cliente: ").capitalize()
            if nome.strip():
                cliente["nome"] = nome
                break
            else:
                print("Erro: O nome não pode ser vazio.")
        while True:
            cpf = input("Digite o cpf do cliente: ")
            if validar_cpf(cpf):
                cliente["cpf"] = cpf.replace(".", "").replace("-", "").strip()
                break
            else:
               print("Erro: CPF inválido. Deve conter 11 números.") 
        while True:
            tel = input("Digite o número de telefone do cliente (COM DDD): ")
            if validar_telefone(tel):
                cliente["tel"] = tel.replace("(", "").replace(")", "").replace("-", "").replace(" ", "").strip()
                break
            else:
                print("Erro: Telefone inválido. Deve ter 10 ou 11 números (DDD + Número).")
        while True:
            end = input("Diite o endereço do cliente: ")
            if end.strip():
                cliente["end"] = end
                break
            else:
                print("Erro: O endereço não pode ser vazio.")
        clientes.append(cliente)
        print("\n✅ Cliente cadastrado com sucesso!\n")
        cmais = input("Deseja adicionar um novo cliente? [S] para sim e [N] para não: ")
        if cmais.upper() == "S":
            print()
        elif cmais.upper() == "N":
            break
        else:
            print("Opção inválida! Digite S ou N.")
    print("\n--- Cadastro encerrado ---")
    if not clientes:
        print("Nenhum cliente foi cadastrado.")
        return # Termina a função se não houver clientes
    while True:
        lclientes = input("Deseja mostrar a lista de clientes cadastrados? [S] para sim / [N] para não: ")
        if lclientes.upper() == "S":
            print("\n----- LISTA DE CLIENTES CADASTRADOS -----")
            print()
            for cliente in clientes:
                print(f"--- Cliente {cliente["nome"]} ---")
                print(f"Nome: {cliente['nome']}")
                print(f"CPF: {cliente['cpf']}")
                print(f"Telefone: {cliente['tel']}")
                print(f"Endereço: {cliente['end']}\n")
            break
        elif lclientes.upper() == "N":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Digite S ou N.")