def show_menu():
    print("\n📝 To-Do List Menu")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if not tasks:
                print("No tasks yet!")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter the task: ")
            tasks.append(task)
            print("✅ Task added.")

        elif choice == "3":
            if not tasks:
                print("Nothing to remove.")
            else:
                try:
                    task_num = int(input("Enter task number to remove: "))
                    removed = tasks.pop(task_num - 1)
                    print(f"❌ Removed: {removed}")
                except (IndexError, ValueError):
                    print("⚠️ Invalid task number.")

        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("⚠️ Please choose a valid option (1-4).")

# Run the app
main()
