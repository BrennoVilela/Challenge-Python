import os

clientes = []
veiculos = []
servicos = []

def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

def validar_placa(placa):
    return len(placa) == 7 and placa.isalnum()

def validar_nome(nome):
    return nome.replace(" ", "").isalpha()

def validar_entrada_numero(numero):
    try:
        return int(numero)
    except ValueError:
        print("Entrada inválida. Deve ser um número.")
        return None

def adicionar_cliente():
    try:
        nome = input("Nome do Cliente: ").strip()
        if not validar_nome(nome):
            raise ValueError("Nome inválido. Deve conter apenas letras.")
        
        cpf = input("CPF do Cliente: ").strip()
        if not validar_cpf(cpf):
            raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")
        
        clientes.append({"nome": nome, "cpf": cpf})
        print("Cliente adicionado com sucesso!")
    
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("Processo de adição de cliente finalizado.")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for idx, cliente in enumerate(clientes, 1):
        print(f"{idx} - Nome: {cliente['nome']}, CPF: {cliente['cpf']}")

def alterar_cliente():
    listar_clientes()
    idx = validar_entrada_numero(input("Escolha o cliente pelo número: "))
    if idx and 1 <= idx <= len(clientes):
        try:
            nome = input("Novo nome: ").strip()
            if not validar_nome(nome):
                raise ValueError("Nome inválido. Deve conter apenas letras.")
            clientes[idx-1]['nome'] = nome
            print("Cliente atualizado com sucesso.")
        except ValueError as ve:
            print(ve)

def excluir_cliente():
    listar_clientes()
    idx = validar_entrada_numero(input("Escolha o cliente pelo número para excluir: "))
    if idx and 1 <= idx <= len(clientes):
        try:
            clientes.pop(idx-1)
            print("Cliente excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir: {e}")

def adicionar_veiculo():
    try:
        listar_clientes()
        cliente_idx = validar_entrada_numero(input("Escolha o cliente para o veículo: "))
        if cliente_idx and 1 <= cliente_idx <= len(clientes):
            placa = input("Placa do Veículo: ").strip().upper()
            if not validar_placa(placa):
                raise ValueError("Placa inválida. Deve ter 7 caracteres alfanuméricos.")
            
            modelo = input("Modelo do Veículo: ").strip()
            veiculos.append({"placa": placa, "modelo": modelo, "cliente": clientes[cliente_idx - 1]})
            print("Veículo adicionado com sucesso.")
        else:
            print("Cliente inválido.")
    
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("Processo de adição de veículo finalizado.")

def listar_veiculos():
    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return
    for idx, veiculo in enumerate(veiculos, 1):
        print(f"{idx} - Placa: {veiculo['placa']}, Modelo: {veiculo['modelo']}, Cliente: {veiculo['cliente']['nome']}")

def alterar_veiculo():
    listar_veiculos()
    idx = validar_entrada_numero(input("Escolha o veículo pelo número: "))
    if idx and 1 <= idx <= len(veiculos):
        try:
            novo_modelo = input("Novo modelo: ").strip()
            veiculos[idx-1]['modelo'] = novo_modelo
            print("Veículo atualizado com sucesso.")
        except ValueError as ve:
            print(ve)

def excluir_veiculo():
    listar_veiculos()
    idx = validar_entrada_numero(input("Escolha o veículo pelo número para excluir: "))
    if idx and 1 <= idx <= len(veiculos):
        try:
            veiculos.pop(idx-1)
            print("Veículo excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir: {e}")

def menu_clientes():
    while True:
        print("\n--- Menu Clientes ---")
        print("1 - Adicionar Cliente")
        print("2 - Listar Clientes")
        print("3 - Alterar Cliente")
        print("4 - Excluir Cliente")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            alterar_cliente()
        elif opcao == '4':
            excluir_cliente()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_veiculos():
    while True:
        print("\n--- Menu Veículos ---")
        print("1 - Adicionar Veículo")
        print("2 - Listar Veículos")
        print("3 - Alterar Veículo")
        print("4 - Excluir Veículo")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            adicionar_veiculo()
        elif opcao == '2':
            listar_veiculos()
        elif opcao == '3':
            alterar_veiculo()
        elif opcao == '4':
            excluir_veiculo()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def main_menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1 - Gerenciar Clientes")
        print("2 - Gerenciar Veículos")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            menu_clientes()
        elif opcao == '2':
            menu_veiculos()
        elif opcao == '0':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
