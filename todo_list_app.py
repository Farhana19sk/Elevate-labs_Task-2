"""
Console-Based To-Do List Application
Persistent storage using a text file.
"""

FILE_NAME = "tasks.txt"


# ----------------------------
# File Handling Functions
# ----------------------------

def load_tasks():
    """Load tasks from the text file."""
    try:
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        # If file doesn't exist, return empty list
        return []


def save_tasks(tasks):
    """Save tasks to the text file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# ----------------------------
# To-Do Functionalities
# ----------------------------

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print() 

def add_task(tasks):
    """Add a new task."""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!\n")
    else:
        print("Task cannot be empty.\n")


def remove_task(tasks):
    """Remove a task by number."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# ----------------------------
# Main Program (CLI Menu)
# ----------------------------

def main():
    tasks = load_tasks()

    while True:
        print("====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.\n")


if __name__ == "__main__":
    main()