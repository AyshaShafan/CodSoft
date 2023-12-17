# To-Do List Application

tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")

def mark_task_complete():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        tasks[task_index]["completed"] = True
        print("Task marked as complete!")
    except (ValueError, IndexError):
        print("Invalid input or task number does not exist.")

def edit_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to edit: ")) - 1
        new_task = input("Enter the new task: ")
        tasks[task_index]["task"] = new_task
        print("Task edited successfully!")
    except (ValueError, IndexError):
        print("Invalid input or task number does not exist.")

def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        del tasks[task_index]
        print("Task deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid input or task number does not exist.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting the To-Do List application. Bye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-6).")

if __name__ == "__main__":
    main()
