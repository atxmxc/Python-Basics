#errors will always happen
#you cant get around them but depending on how your program is structured, it can either handle them well or crash
#exceptions is like python saying i cant do this safely
int("hello") #this will return a ValueError

#try and except
#this is when the code tries to execute some code and if it gets some error, it will handle it.
try:
    risky_code
except SomeError:
    handle_it

#here it is in action

try:
    age = int(input("Age: ").strip())
except ValueError:
    print("Enter A Valid Number: ")

#here is another one exccept catching multiple errors
try:
    value = int(input())
except (ValueError, TypeError):
    print("Invalid Input")

#here is one using else & finally
try:
    num = int(input())
except ValueError:
    print("Error")
else:
    print("Success")
finally:
    print("Done")
    
