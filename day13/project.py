#day09; modifying day08 to do list to incorporate json
import json
import csv
import argparse

parser = argparse.ArgumentParser(description="Additional Command Line For Easier Use")

parser.add_argument("--add", help="Add Tasks")
parser.add_argument("--mark", help="Mark Of Tasks")
parser.add_argument("--remove", help="remove tasks")
parser.add_argument("--view", action="store_true", help="View tasks")
parser.add_argument("--export", action="store_true", help="Export tasks to CSV")

args = parser.parse_args()

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

def export_all_tasks():
    with open("tasks.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'done'])
        writer.writeheader()
        for task in tasks:
            writer.writerow(task)

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
    for i, task in enumerate(tasks):
        if task.get("title") == title:
            del tasks[i]
            return True
    return False

def log_app(message):
    with open("todo.log", "a", encoding="utf-8") as f:
        f.write(message + "\n")


tasks = []
load_tasks()

# print("======To Do List======")
# print("Usage:")
# print("-----------------")
# print("Add Tasks: add, Remove Task: remove, View Tasks: view, Export Tasks: export, Exit Program: exit")
# print("----------------------------------------------------------------------------")
# print(f"Loaded {len(tasks)} tasks.")
# print("--------------------------------")

# while True:
#     try:
#         now = input("Enter What You Would Like To Do: ").lower().strip()
#     except KeyboardInterrupt:
#         print("\nExiting Safely!")
#         break

#     if now == "add":
#         title = input("Please Enter The Task Name: ").strip()
#         if not title:
#             print("Task Cannot Be Empty.")
#             continue
#         add_tasks(title)
#         log_app(f"User Has Added A Task: {title}")
#         print("Task Successfully added")
#         save_tasks()

#     elif now == "remove":
#         title = input("Please Enter the Name of the task: ").strip()
#         if remove_task(title):
#             log_app(f"User Has Removed A Task: {title}")
#             print("Task Removed")
#             save_tasks()
#         else:
#             print("Invalid Task")
#     elif now == "view":
#         view_tasks()

#     elif now == "mark":
#         title = input("Enter The Name Of the Task: ")
#         if mark_tasks(title):
#             log_app(f"User Has Marked Task As Complete: {title}")
#             print("Task Marked Completed")
#             save_tasks()
#         else:
#             print("Invalid Task")
#     elif now == 'export':
#         export_all_tasks()
#         print("Tasks Exported Successfully")

#     elif now == "exit":
#         confirm = input("Are You Sure You Want To Exit?: ").strip().lower()
#         if confirm == 'yes':
#             log_app("User Has Exited Program. STATUS CODE: 200")
#             break
#         else:
#             continue
if args.add:
    add_tasks(args.add)
    save_tasks()
    log_app(f"Task Added: {args.add}")
elif args.mark:
    mark_tasks(args.mark)
    save_tasks()
    log_app(f"Task Marked As Done: {args.mark}")
elif args.remove:
    remove_task(args.remove)
    save_tasks()
    log_app(f"Task Removed: {args.remove}")
elif args.view:
    view_tasks()
elif args.export:
    try:
        export_all_tasks()
        log_app("Tasks Successfuly exported")
    except FileNotFoundError:
        print("Failed To Export: Make Sure File Exists")
else:
    parser.print_help()
    