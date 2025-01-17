def todo_list():
    print("Bem-vindo ao To-Do List!")
    tasks = []

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Listar tarefas")
        print("4. Sair")

        try:
            choice = int(input("Digite o número da opção desejada: "))

            if choice == 1:
                task = input("Digite a descrição da tarefa: ").strip()
                if task:
                    tasks.append(task)
                    print(f"Tarefa '{task}' adicionada com sucesso!")
                else:
                    print("Erro: A descrição da tarefa não pode estar vazia.")

            elif choice == 2:
                if not tasks:
                    print("Nenhuma tarefa para remover.")
                else:
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                    try:
                        task_num = int(input("Digite o número da tarefa que deseja remover: "))
                        if 1 <= task_num <= len(tasks):
                            removed_task = tasks.pop(task_num - 1)
                            print(f"Tarefa '{removed_task}' removida com sucesso!")
                        else:
                            print("Erro: Número inválido.")
                    except ValueError:
                        print("Erro: Por favor, insira um número válido.")

            elif choice == 3:
                if not tasks:
                    print("Nenhuma tarefa na lista.")
                else:
                    print("\nTarefas:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")

            elif choice == 4:
                print("Saindo do programa. Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Erro: Por favor, insira um número válido.")

# Executa o programa de To-Do List
if __name__ == "__main__":
    todo_list()
