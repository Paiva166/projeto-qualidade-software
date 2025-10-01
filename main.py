# Sistema de Tarefas - Versão 1.0

def mostrar_menu():
    print("\n=== SISTEMA DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Sair")
    return input("Escolha uma opção: ")

def main():
    tarefas = []
    
    while True:
        opcao = mostrar_menu()
        
        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            if tarefa.strip():
                tarefas.append({"tarefa": tarefa, "concluida": False})
                print("Tarefa adicionada!")
            else:
                print("Erro: Tarefa não pode estar vazia!")
        
        elif opcao == "2":
            print("\n--- SUAS TAREFAS ---")
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i, tarefa in enumerate(tarefas, 1):
                    status = "✓" if tarefa["concluida"] else " "
                    print(f"{i}. [{status}] {tarefa['tarefa']}")
        
        elif opcao == "3":
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()