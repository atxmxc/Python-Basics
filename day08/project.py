#day08; a better to do list
tasks = []

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
    for i, task in enumerate(tasks):
        if task.get("title") == title:
            del tasks[i]
            return True
    return False

print("======To Do List======")
print("Usage:")
print("-----------------")
print("Add Tasks: add, Remove Task: remove, View Tasks: view, Exit Program: exit")
print("----------------------------------------------------------------------------")
while True:
    now = input("Enter What You Would Like To Do: ").lower().strip()
    if now == "add":
        title = input("Please Enter The Task Name: ").strip()
        add_tasks(title)
        print("Task Successfully added")
    elif now == "remove":
        title = input("Please Enter the Name of the task: ").strip()
        if remove_task(title):
            print("Task Removed")
        else:
            print("Invalid Task")
    elif now == "view":
        view_tasks()
    elif now == "mark":
        title = input("Enter The Name Of the Task: ")
        if mark_tasks(title):
            print("Task Marked Completed")
        else:
            print("Invalid Task")
    elif now == "exit":
        confirm = input("Are You Sure You Want To Exit?: ").strip().lower()
        if confirm == 'yes':
            break
        else:
            continue


