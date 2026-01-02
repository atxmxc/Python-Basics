# file & folder automation
# python is useful as it allows us to tell the computer to do the boring things over and over again.
# we now use another library called os
import shutil
import os
# get current file directory
print(os.getcwd())
# we can list the files in a the folder
files = os.listdir(".")

for file in files:
    print(file)

# we can check to see if something is a file or folder
for name in os.listdir("."):
    if os.path.isfile(name):
        print(f"File: {name}")
    elif os.path.isdir(name):
        print(f"Folder: {name}")
# we can also rename files with the os library
'os.rename("notes.txt", "os.txt")'
# we can also rename them in bulk
for i, file in enumerate(os.listdir("."), start=1):
    if file.endswith(".txt"):
        os.rename(file, f"note_{i}.txt")
# we can also move files using the shutil library
shutil.move("note_19.txt.", "day14/note19.txt")
