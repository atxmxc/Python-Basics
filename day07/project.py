#day07 simple project; contact book
contacts = {}

def get_job(prompt):
    return input(prompt).lower()

def add_contact(name, num):
    contacts[name] = num

def remove_contact(name):
    contacts.pop(name, None)

print("=====Contact Book=====")
print("Tips on How To Use:")
print("----------------------------")
print("View Contacts: view, Add Contacts: add, Remove Contacts: remove, Exit Program: exit")
print("---------------------------------------------------------------------------------------")
while True:
    now = input("What Would You Like To Do In Your Contacts Book?: ").strip().lower()
    if now == "view":
        print(f"You Have {len(contacts)} in your contacts")
        confirm =  input("Would You Like To View Your Contacts?: ")
        if confirm.lower() == 'yes':
            for k,v in contacts.items():
                print(k, v)
        else:
            continue
    elif now == "add":
        name = get_job("Enter The Name: ")
        if not name:
            print("Invalid")
            continue
        num = get_job('Enter Number: ')
        if not num:
            print('Invalid')
            continue
        add_contact(name, num)
        print("Contact Added")
    elif now == 'remove':
        name = get_job("Please Enter The Name of the Contact: ")
        if name in contacts:
            remove_contact(name)
            print(f"Contact Removed: {name}")
        else:
            print(f"Failed To remove contact; no contact named {name}")
            continue
    elif now == 'exit':
        confirmation = input("Are You Sure You Want To Quit?: ").strip()
        if confirmation.lower() == 'yes':
            break
        else:
            continue
        



