def Cadastros():
    import json
    import os


    def validar_cpf(cpf):
        cpf_limpo = cpf.replace(".", "").replace("-", "").strip()
        if len(cpf_limpo) == 11 and cpf_limpo.isdigit():
            return True
        return False


    def validar_telefone(tel):
        tel_limpo = tel.replace("(", "").replace(")", "").replace(
            "-", "").replace(" ", "").strip()
        if tel_limpo.isdigit() and 10 <= len(tel_limpo) <= 11:
            return True
        return False


    def buscar_cliente_por_cpf(lista_clientes, cpf_a_buscar):
        for cliente in lista_clientes:
            if cliente['cpf'] == cpf_a_buscar:
                return cliente  # Encontrou, retorna o cliente
        return None  # Não encontrou, retorna None


    def validar_email(email):
        if '@' in email and '.' in email:
            return True
        return False


    def cadastrar_novo_cliente(lista_clientes):
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
                    cliente["tel"] = tel.replace("(", "").replace(")", "").replace(
                        "-", "").replace(" ", "").strip()
                    break
                else:
                    print(
                        "Erro: Telefone inválido. Deve ter 10 ou 11 números (DDD + Número).")
            while True:
                email = input("Digite o e-mail do cliente: ")
                if validar_email(email):
                    cliente["email"] = email
                    break
                else:
                    print("Erro: digite um e-mail válido!")
            while True:
                end = input("Diite o endereço do cliente: ")
                if end.strip():
                    cliente["end"] = end
                    break
                else:
                    print("Erro: O endereço não pode ser vazio.")
            clientes.append(cliente)
            print("\n✅ Cliente cadastrado com sucesso!\n")
            while True:
                nCD = input("Deseja cadastrar outro cliente? [S/N]: ")
                if nCD.upper() == "S":
                    print()
                    break
                elif nCD.upper() == "N":
                    print()
                    return
                else:
                    print("Opção inválida! Digite 'S' ou 'N'!")


    nome_arquivo = 'clientes.json'

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Tenta carregar os dados JSON para a lista 'clientes'
            clientes = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        clientes = []
    print(f">>>>> SISTEMA DE CADASTRO DE NOVOS CLIENTES <<<<<")
    print(f"Atualmente, há {len(clientes)} cliente(s) cadastrado(s).\n")
    while True:
        print("===== MENU PRINCIPAL =====")
        print("1. Cadastrar um novo cliente")
        print("2. Buscar cliente por CPF")
        print("3. Listar todos os clientes")
        print("4. Alterar dados de um cliente")
        print("5. Apagar um cliente")
        print("6. Sair e salvar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print()
            cadastrar_novo_cliente(clientes)

        elif opcao == '2':
            if not clientes:
                print("\nNão há clientes cadastrados para buscar.\n")
            else:
                cpf_procurado = input("\nDigite o CPF do cliente que deseja buscar: ")
                cpf_limpo = "".join(filter(str.isdigit, cpf_procurado))
                cliente_encontrado = buscar_cliente_por_cpf(clientes, cpf_limpo)
                if cliente_encontrado:
                    print("\n✅ Cliente Encontrado!")
                    print(f"  Nome: {cliente_encontrado.get('nome', 'N/A')}")
                    print(f"  CPF: {cliente_encontrado.get('cpf', 'N/A')}")
                    print(f"  Telefone: {cliente_encontrado.get('tel', 'N/A')}")
                    print(f"  E-mail: {cliente_encontrado.get('email', 'N/A')}")
                    print(f"  Endereço: {cliente_encontrado.get('end', 'N/A')}\n")
                else:
                    print("\n❌ Cliente não encontrado com o CPF informado.\n")

        elif opcao == '3':
            print("\n----- LISTA DE CLIENTES CADASTRADOS -----")
            print()
            for cliente in clientes:
                print(f"--- Cliente {cliente["nome"]} ---")
                print(f"Nome: {cliente['nome']}")
                print(f"CPF: {cliente['cpf']}")
                print(f"Telefone: {cliente['tel']}")
                print(f"Endereço: {cliente['end']}\n")
            break
        elif opcao == '4':
            if not clientes:
                print("\nNão há clientes cadastrados para alterar os dados.\n")
            else:
                cpf_procurado = input("\nDigite o CPF do cliente que deseja alterar os dados: ")
                cpf_limpo = "".join(filter(str.isdigit, cpf_procurado))
                cliente_encontrado = buscar_cliente_por_cpf(clientes, cpf_limpo)
                if cliente_encontrado:
                    while True:
                        print("\n--- Alterando Cliente ---")
                        print(f"Nome: {cliente_encontrado['nome']}")
                        print(f"Telefone: {cliente_encontrado.get('tel', 'N/A')}")
                        print(f"E-mail: {cliente_encontrado.get('email', 'N/A')}")
                        print(f"Endereço: {cliente_encontrado.get('end', 'N/A')}")
                        print("-------------------------")
                        print()
                        print("O que você deseja alterar?")
                        print("1. Nome")
                        print("2. Telefone")
                        print("3. E-mail")
                        print("4. Endereço")
                        print("5. Voltar ao menu principal")
                        escolha_alteracao = input("Escolha o campo para alterar: ")
                        if escolha_alteracao == '1':
                            novo_nome = input(f"Digite o novo nome: ").capitalize()
                            if novo_nome.strip():
                                cliente_encontrado['nome'] = novo_nome.strip()
                                print("✅ Nome alterado com sucesso!")
                            else:
                                print("❌ Nome não pode ser vazio.")
                        elif escolha_alteracao == '2':
                            novo_telefone = input(f"Digite o novo telefone: ")
                            if validar_telefone(novo_telefone):
                                cliente_encontrado['tel'] = "".join(
                                    filter(str.isdigit, novo_telefone))
                                print("✅ Telefone alterado com sucesso!")
                            else:
                                print()
                                print("❌ Telefone inválido.")
                        elif escolha_alteracao == '3':
                            novo_email = input(f"Digite o novo e-mail: ")
                            if validar_email(novo_email):
                                novo_email.strip()
                                cliente_encontrado['email'] = novo_email
                                print("✅ E-mail alterado com sucesso!")
                            else:
                                print()
                                print("❌ Digite um e-mail válido!")

                        elif escolha_alteracao == '4':
                            novo_endereco = input(f"Digite o novo endereço: ")
                            if novo_endereco.strip():
                                cliente_encontrado['end'] = novo_endereco
                                print("✅ Endereço alterado com sucesso!")
                            else:
                                print()
                                print("❌ Endereço não pode ser vazio.")

                        elif escolha_alteracao == '5':
                            print("Voltando ao menu principal...\n")
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                else:
                    print("\n❌ Cliente não encontrado com o CPF informado.\n")
        elif opcao == '5':
            if not clientes:
                print("\nNão há clientes cadastrados para apagar os dados.\n")
            else:
                cpf_procurado = input(
                    "\nDigite o CPF do cliente que deseja deletar do sistema: ")
                cpf_limpo = "".join(filter(str.isdigit, cpf_procurado))
                cliente_encontrado = buscar_cliente_por_cpf(clientes, cpf_limpo)
                if cliente_encontrado:
                    while True:
                        apagar = input(
                            "Você tem certeza que deseja apagar este cliente? [S/N]: ")
                        if apagar.upper() == 'S':
                            clientes.remove(cliente_encontrado)
                            print("\n✅ Cliente apagado com sucesso!\n")
                            break
                        elif apagar.upper() == 'N':
                            print("\nOperação cancelada.\n")
                            break
                        else:
                            print("\nOpção inválida! Tente novamente!\n")
                else:
                    print("\nCPF digitado inválido ou não encontrado!\n")
        elif opcao == '6':
            # Salva a lista completa (com as alterações) no arquivo ANTES de sair
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
            print("\nDados salvos com sucesso. Saindo do programa...")
            break

        else:
            print("\nOpção inválida! Por favor, escolha uma opção de 1 a 5.\n")
