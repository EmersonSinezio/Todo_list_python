from models.todo import Todo

def show_menu():
    print("\n--- To-Do List ---")
    print("1 - Adicionar tarefa")
    print("2 - Mostrar todas as tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

def add_task():
    task = input("Digite a tarefa: ")
    todo = Todo(task)
    todo.save()
    print(f"Tarefa '{task}' adicionada com sucesso!")

def show_tasks():
    tasks = Todo.get_all()
    if tasks:
        for i, task in enumerate(tasks):
            status = "Concluída" if task['completed'] else "Pendente"
            print(f"{i+1} - {task['task']} (ID: {task['id']}) - {status}")
    else:
        print("Nenhuma tarefa encontrada.")

def mark_task_as_completed():
    task_id = input("Digite o ID da tarefa que deseja marcar como concluída: ")
    Todo.mark_completed(task_id)

def remove_task():
    task_id = input("Digite o ID da tarefa que deseja remover: ")
    Todo.remove(task_id)
