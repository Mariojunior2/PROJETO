def adicionar_tarefa(Nometf, tarefa):
    tarefa[Nometf] = {
        "Tarefa": Nometf,
    }
    print(f"Tarefa {Nometf} adicionado com sucesso")
    
def remover_tarefa(Nometf, tarefa):
    if Nometf in tarefa:
        del tarefa[Nometf]
        print(f"Tarefa {Nometf} removida")
    else:
        print("Erro")

def listar_tarefa(tarefa):
    if tarefa:
        for Nometf in tarefa.items():
           print(f"Lista de Tarefas{Nometf}")
    else:
        print("Nenhuma Tarefa")

def exibir_menu():
    print("==== Gerenciador de Tarefas ====")
    print("1 - Adicionar Tarefas")
    print("2 - Remover Tarefa")
    print("3 - Listar Tarefas")
    print("4 - Sair")

tarefa: dict[str, dict[str, str]] = {}

while True:
    exibir_menu()
    opcao = input("Escolha: ")
    if opcao == "1":
        Nometf = input("Nome da Tarefa: ")
        adicionar_tarefa(Nometf, tarefa)
    elif opcao == "2":
        Nometf = input("Fale o nome da tarefa para remover: ")
        remover_tarefa(Nometf, tarefa)
    elif opcao == "3":
        listar_tarefa(tarefa)
    elif opcao == "4":
        print("Saindo")
        break
    