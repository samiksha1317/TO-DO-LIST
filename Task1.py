tasks = []

def show_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tasks.append(input("Enter task: "))
        print("Task added!")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        idx = int(input("Enter task number to update: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx] = input("Enter new task: ")
            print("Task updated!")
        else:
            print("Invalid task number!")
    elif choice == "4":
        show_tasks()
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("Task deleted!")
        else:
            print("Invalid task number!")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")
