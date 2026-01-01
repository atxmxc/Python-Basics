#day09; modifying day08 to do list to incorporate json
import json

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def add_tasks(title):
    tasks.append({"title": title, "done": False})

def mark_tasks(title):
    for task in tasks:
        if task["title"] == title:
            task["done"] = True
            return True
    return False

def view_tasks():
    if not tasks:
        print("There are no tasks in your to-do list.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "done" if task["done"] else "todo"
        print(f'{i}. {task["title"]} [{status}]')
    
def remove_task(title):
    try:
        for i, task in enumerate(tasks):
            if task.get("title") == title:
                del tasks[i]
                return True
        return False
    except ValueError:
        print("Unsuccessful")



tasks = []
load_tasks()

print("======To Do List======")
print("Usage:")
print("-----------------")
print("Add Tasks: add, Remove Task: remove, View Tasks: view, Exit Program: exit")
print("----------------------------------------------------------------------------")
print(f"Loaded {len(tasks)} tasks.")
print("--------------------------------")
while True:
    try:
        now = input("Enter What You Would Like To Do: ").lower().strip()
    except KeyboardInterrupt:
        print("\nExiting Safely!")
        break

    if now == "add":
        title = input("Please Enter The Task Name: ").strip()
        if not title:
            print("Task Cannot Be Empty.")
            continue
        add_tasks(title)
        print("Task Successfully added")
        save_tasks()
    elif now == "remove":
        title = input("Please Enter the Name of the task: ").strip()
        if remove_task(title):
            print("Task Removed")
            save_tasks()
        else:
            print("Invalid Task")
    elif now == "view":
        view_tasks()
    elif now == "mark":
        title = input("Enter The Name Of the Task: ")
        if mark_tasks(title):
            print("Task Marked Completed")
            save_tasks()
        else:
            print("Invalid Task")
    elif now == "exit":
        confirm = input("Are You Sure You Want To Exit?: ").strip().lower()
        if confirm == 'yes':
            break
        else:
            continue


