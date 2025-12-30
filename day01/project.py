#First Basic Project. An Info Inputter and Outputter.
print("==========Personal==Info==Inputter/Outputter========")
#name
firstname = input("Enter Your First Name: ")
middlename = input("Enter Your Middle Name: [leave empty if none]")
lastname = input("Enter Last Name: ")

#age
year = int(input("Enter Current Year: "))
age = int(input("Please Enter Your Age: "))
yearBorn = year - age

print(f'Hello {firstname} {middlename} {lastname}')
print(f'You are {age} years old and was born in {yearBorn}')
