#functions
#functions are blocks of code that do one job
#when needed, you call the function instead of repeating the code over and over.
#basic structure of a fucntion
# def say_hello():
#     print("Hello World")

# say_hello() #if you dont call the fucntion like this, nothing will happen and you will have no output from it
#you can also add parameters to your function
def greet(name):
    print(f'hello {name}')

greet('Andy')