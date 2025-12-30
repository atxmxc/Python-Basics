#simple project combining topics from today. An Age Sorter.
print("========Age=Sorter=========")
age = int(input("Please Enter Your Age: ").strip())
if age < 0:
    print("Invalid Age")
elif age < 13:
    print("You are a child")
elif age >= 13 and age < 18:
    print("You are a teenager")
elif age >= 18 and age < 25:
    print("You are a young adult")
elif age >=25 and age < 50:
    print("You are an adult")
else:
    print("You are a senior")

print(f"Age Entered: {age}")