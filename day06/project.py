#day06 project; a simple to do list
tasks = []
def get_task(prompt):
    return str(input(prompt))

def add_task(task):
    return tasks.append(task)

def remove_tasks(task):
    return tasks.remove(task)

print('=====To Do List=====')
print("Help Tips")
print("View Tasks: View, Add Tasks: Add, Remove Task: Remove, Exit: exit")
print('-----------------')
while True:
    now = input("What Would You Like To Do?: ").strip()
    if now.lower() == 'view':
        print(f'You Have {len(tasks)} tasks in Your To Do list')
        advance = input("Would You Like To See the tasks due?: [yes/no]").strip()
        if advance.lower() == 'yes':
            print(*tasks, sep=', ')
        else:
            continue
            
    elif now.lower() == 'add':
        todo = get_task('Please Enter A Task: ').strip()
        print('Task Added')
        add_task(todo)

    elif now.lower() == "remove":
        what = get_task('Please Enter The Task You Wish To Remove: ')
        print("Task Removed")
        remove_tasks(what)
    
    elif now.lower() == 'exit':
        exit = input("Would You Like To Quit?: ")
        if exit.lower() == 'yes':
            break
        else:
            continue

    

