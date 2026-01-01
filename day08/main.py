#day08; combining dictionaries, lists and loops + functions
#a list can hold many items while a dictionary describes one item
users = [
    {"name": "andrew", "age": 14},
    {"name": "alex", "age": 16}
]
#another example but in the form of a to do list
tasks = [
    {"title": "homework", "done": False},
    {"title": "gym", "done": True}
]
#looping through it
for hw in tasks:
    print(hw["title"], hw["done"])

#searching
target = "homework"
for hw in tasks:
    if hw["title"] == target:
        print("Found it")

#removing
tasks = [t for t in tasks if t["title"] != target]
#or
for i, t in enumerate(tasks):
    if t.get("title") == target:
        tasks.pop(i)
        break