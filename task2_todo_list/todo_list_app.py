#to do list program
import json
import os

def load_tasks():
    if os.path.exists("todo.json"):
        with open("todo.json", "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open("todo.json", "w") as f:
        json.dump(tasks, f, indent=4)

def show_menu():
    print("\n📝 TO-DO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark as Done")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i+1}. [{status}] {t['task']}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

        save_tasks(tasks)

if __name__ == "__main__":
    main()
