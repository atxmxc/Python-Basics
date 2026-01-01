#json
#json looks like python dicts and lists but its different
# [
#   {"title": "homework", "done": false},
#   {"title": "gym", "done": true}
# ]
#however, python <---> json
#now we can use our first import; import json
import json
#saving data
# tasks = 4
# with open("tasks.json", "w") as g:
#     json.dump(tasks, g)

#loading data from a file
with open("tasks.json", "r") as g:
    tasks = json.load(g)