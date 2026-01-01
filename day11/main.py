#file handling and simple logs
#a bit like json except we are reading and handling .txt files
with open("day11/notes.txt", "r", encoding="utf-8") as g:
    text = g.read()

print("CONTENT START")
print(repr(text))
print("CONTENT END")
#reading line by line
# with open("day11/notes.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

#writing a text file
with open("day11/notes.txt", "w", encoding="utf-8") as h:
    h.write("Hello\n")


#appending(logging)
with open("apps.log", "a", encoding="utf-8") as s:
    s.write("User Has Logged In: 19:04:23\n")

#we can also handle files if they are missing
try:
    with open("hah.txt", "r", encoding="utf-8") as d:
        print(f.read())
except FileNotFoundError:
    print("File Not Found")