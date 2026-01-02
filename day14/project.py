# day14; a simple file mover
import os
import shutil

BASE_DIR = "files"

folders = {
    ".txt": "text_files",
    ".json": "jsonfiles",
    ".csv": "csv__files"
}

os.makedirs(BASE_DIR, exist_ok=True)

for file in os.listdir("."):
    if not os.path.isfile(file):
        continue
    ext = os.path.splitext(file)[1]
    target = folders.get(ext, "other")

    target_path = os.path.join(BASE_DIR, target)
    os.makedirs(target_path, exist_ok=True)

    shutil.move(file, os.path.join(target_path, file))
    print(f"Moved {file} to {target}")
