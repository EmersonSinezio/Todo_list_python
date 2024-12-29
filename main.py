from views.todo_view import show_menu, add_task, show_tasks, mark_task_as_completed, remove_task

#TODO - Remover o gerenciamento por id pois está dando muitos bugs
def main():
    while True:
        show_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_task_as_completed()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()