import json
import os
import re

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
# Cria o caminho completo para o clientes.json, que está NA MESMA PASTA
nome_arquivo = os.path.join(DIRETORIO_ATUAL, 'clientes.json')

def validar_cpf(cpf: str) -> bool:
    cpf_limpo = "".join(filter(str.isdigit, cpf))
    if len(cpf_limpo) != 11:
        return False
    if len(set(cpf_limpo)) == 1:
        return False
    # 4. Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf_limpo[i]) * (10 - i)
    resto = (soma * 10) % 11
    if resto == 10:  # Se o resto for 10, o dígito é 0
        resto = 0
    if resto != int(cpf_limpo[9]):
        return False  # Primeiro dígito verificador inválido
    # 5. Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf_limpo[i]) * (11 - i)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf_limpo[10]):
        return False  # Segundo dígito verificador inválido

    # Se passou por tudo, o CPF é válido
    return True

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
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    return False

def enc_cliente(lista_clientes):
    cpf_procurado = input("\nDigite o CPF do cliente: ")
    cpf_limpo = "".join(filter(str.isdigit, cpf_procurado))
    
    cliente_encontrado = buscar_cliente_por_cpf(lista_clientes, cpf_limpo)
    
    if not cliente_encontrado:
        print("\n❌ Cliente não encontrado com o CPF informado.\n")
        return None
        
    return cliente_encontrado

def cadastrar_novo_cliente(lista_clientes):
        while True:
            cliente = {}
            while True:
                nome = input("Digite o nome do cliente: ").capitalize()
                nome_sem_esp = nome.replace(" ", "")
                if not nome:
                    print("Erro: O nome não pode ser vazio.")
                elif not nome_sem_esp.isalpha():
                    print("Erro: O nome deve conter apenas letras e espaços.")
                else:
                    cliente["nome"] = nome
                    break
            while True:
                cpf = input("Digite o cpf do cliente: ")
                if validar_cpf(cpf): 
                    cpf_limpo = "".join(filter(str.isdigit, cpf))
                    if buscar_cliente_por_cpf(lista_clientes, cpf_limpo):
                        print("Erro: Já existe um cliente cadastrado com este CPF.")
                    else:
                        cliente["cpf"] = cpf_limpo
                        break
                else:
                    print("Erro: CPF inválido. Verifique os números e tente novamente.")
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
                end = input("Digite o endereço do cliente: ")
                if end.strip():
                    cliente["end"] = end
                    break
                else:
                    print("Erro: O endereço não pode ser vazio.")
            lista_clientes.append(cliente)
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

def Cadastros():
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
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
                cliente = enc_cliente(clientes)
                if cliente:
                    print("\n✅ Cliente Encontrado!")
                    print(f"  Nome: {cliente.get('nome', 'N/A')}")
                    print(f"  CPF: {cliente.get('cpf', 'N/A')}")
                    print(f"  Telefone: {cliente.get('tel', 'N/A')}")
                    print(f"  E-mail: {cliente.get('email', 'N/A')}")
                    print(f"  Endereço: {cliente.get('end', 'N/A')}\n")
                else:
                    print("\n❌ Cliente não encontrado com o CPF informado.\n")
        elif opcao == '3':
            if not clientes:
                print("\nNão há clientes cadastrados para listar.\n")
            else:
                print("\n----- LISTA DE CLIENTES CADASTRADOS -----")
                print()
                for cliente in clientes:
                 print(f"--- Cliente {cliente["nome"]} ---")
                 print(f"Nome: {cliente['nome']}")
                 print(f"CPF: {cliente['cpf']}")
                 print(f"Telefone: {cliente['tel']}")
                 print(f"Endereço: {cliente['end']}\n")
                 print("-------------------------")
        elif opcao == '4':
            if not clientes:
                print("\nNão há clientes cadastrados para alterar os dados.\n")
            else:
                cliente = enc_cliente(clientes)
                if cliente:
                    while True:
                        print("\n--- Alterando Cliente ---")
                        print(f"Nome: {cliente['nome']}")
                        print(f"Telefone: {cliente.get('tel', 'N/A')}")
                        print(f"E-mail: {cliente.get('email', 'N/A')}")
                        print(f"Endereço: {cliente.get('end', 'N/A')}")
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
                                cliente['nome'] = novo_nome.strip()
                                print("✅ Nome alterado com sucesso!")
                            else:
                                print()
                                print("❌ Nome não pode ser vazio.")
                        elif escolha_alteracao == '2':
                            novo_telefone = input(f"Digite o novo telefone: ")
                            if validar_telefone(novo_telefone):
                                cliente['tel'] = "".join(
                                    filter(str.isdigit, novo_telefone))
                                print("✅ Telefone alterado com sucesso!")
                            else:
                                print()
                                print("❌ Telefone inválido.")
                        elif escolha_alteracao == '3':
                            novo_email = input(f"Digite o novo e-mail: ")
                            if validar_email(novo_email):
                                novo_email.strip()
                                cliente['email'] = novo_email
                                print("✅ E-mail alterado com sucesso!")
                            else:
                                print()
                                print("❌ Digite um e-mail válido!")

                        elif escolha_alteracao == '4':
                            novo_endereco = input(f"Digite o novo endereço: ")
                            if novo_endereco.strip():
                                cliente['end'] = novo_endereco
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
                    print("\nRetornando ao menu principal...\n")
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
            try:
                # Salva a lista completa (com as alterações) no arquivo ANTES de sair
                with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
                print("\nDados salvos com sucesso. Saindo do programa...")
                break
            except IOError as e:
                print(f"\nErro ao salvar o arquivo: {e}")
                print("Saindo sem salvar.")
            break
        else:
            print("\nOpção inválida! Por favor, escolha uma opção de 1 a 6.\n")
            
if __name__ == "__main__":
    Cadastros()

# testes necessarios conta github
# testes necessarios conta github
# testes necessarios conta github
# testes necessarios conta github
# testes necessarios conta github
# testes necessarios conta github
# testes necessarios conta github
