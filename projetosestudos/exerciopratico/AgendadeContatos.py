def adicionar_contato(agenda, nome, telefone, email):
    agenda[nome] = {
        "nome": nome,
        "telefone": telefone,
        "email": email 
    }
    print(f"Contato {nome} adicionado com sucesso!")

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} removido.")
    else:
        print("Contato nao encontrado")
        
def buscar_contato(agenda, nome,):
    if nome in agenda:
        print(f"Nome: {nome}")
        print(f"Telefone: {agenda[nome]['telefone']}")
        print(f"Email: {agenda[nome]['email']}") 
    else:
        print("Contato inexistente")

def listar_contatos(agenda):
    if agenda:
        for nome, detalhes in agenda.items():
            print(f"Nome: {nome}")
            print(f"Teleforne: {detalhes['telefone']}")
            print(f"E-mail: {detalhes['email']}")
            print("-" * 20)
        else:
            print("A agenda vazia.")

def exibir_menu():
    print("==== Agenda de Contatos ====")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar Contato")
    print("4 - Listar Contatos")
    print("5 - Sair")
    
agenda: dict[str, dict[str, str]] = {}


while True:
    exibir_menu()
    exibir_menu
    opcao = input("Escolha uma opcao: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        telefone =  input("Telefone: ")
        email = input("E-mail: ")
        adicionar_contato(agenda, nome, telefone, email)
    elif opcao == "2":
        nome = input("Nome do contato a remover: ")
        remover_contato(agenda, nome)
    elif opcao == "3":
        nome = input("Nome do contato a buscar: ")
        buscar_contato(agenda, nome)
    elif opcao == "4":
        listar_contatos(agenda)
    elif opcao == "5":
        print("Saindo")
        break