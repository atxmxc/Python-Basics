#day02 of basic python; numbers and operators
#many types of opertors so these are the important ones
'+' #add
'-' #subtract
'*' #multiplication
'/' #division (float)
'//' #integer division (rounds to the nearest whole number)
'**' #power
'%' #remainder

#examples
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)

#multi-operator 
#you can include multiple operators in a single line of code
print((10 * 3) + 2)
print(10 // 2 * 4)
print((4 + 2) / 3)

#differences between input() and int()/float()
age = input('Enter Your Age: ') #this is incorrect, this treats the number as a string, not an integer, so we cannot use math operators without converting to int()
#----------------#
age = int(input("Enter Your Age: ")) #this is correct, the age is now an integer variable, we can now use math operators with it.
age = float(input("Enter Your Age: ")) #this is also correct, age is now a float variable, especially if you want to put 12.5 years old and be more specific.

#using f-strings instead of ("age is", age, "years old")
#this is important as it is alot easier to use and understand as well as it becoming a standard. Important Habit.
print("You are", age, "years old") #this is still going to work but its alot more easier to use f-strings, companies/people who hire will look for this.
print(f'You are {age} years old') #this is much better.

#if statements
#if statements are used to meet a ceratain condition. Once the condition is met, the code inside the indent will be executed.
x = int(input("Enter a number: ").rstrip())
if x > 5:
    print(f'{x} is large than 5')
else:
    print(f'{x} is less than 5')
