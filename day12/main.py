#csv files; reading, writing, appending, understand and using them in real life situations.
#a csv file is just rows of data separated by commas, so it looks something like this
# name,age,done 
# wash clothes,0,True
# wash shoes,0,False

#we now have a new library to use, csv
import csv
#reading from a csv file
with open("tasks.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#writing a csv file(overwriting)
with open("tasks.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'done'])
    writer.writerow(['washclothes', True])

#appending rows(without overwriting the csv file)
with open("tasks.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['cleanshoes', False])

#dict based csv(very useful)
#writing with headers
with open("tasks.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'done'])
    writer.writeheader()
    writer.writerow({"title": "homework", "done": False})

#reading as dictionaries
with open("tasks.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['title'], row['done'])
