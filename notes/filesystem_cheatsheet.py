import os
import shutil

os.listdir(".")
os.getcwd()
os.makedirs("folder", exist_ok=True)
os.path.isfile("file.txt")
os.path.join("a", "b")
os.path.splitext("file.txt")
shutil.move("src", "dst")
shutil.copy("src", "dst")
