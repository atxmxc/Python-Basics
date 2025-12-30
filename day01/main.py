#print function
print("Hello Guys!") 
print(1+2) #just a simple math question
print(2>3) #outputs false as its a boolean.
print(23) #just outputs a number

#variables and assigning them
x1 = 1 #integer variable
x2 = "hello" #string variable
x3 = 1721.34 #float variable

#you can check the class of a variable using the type() function;
print(type(x3))
    #output: <class 'float'>. Works for any variable

#input function and basic conversion
#input() allows you to assign values to a variable when you please, meaning it can be changed every time you run the code. Also, defualt input() will return text.
hi = input("Input Something: ")
print(f'Value: {hi}')
#there are also different conversion types
value = int(input('Enter a number: ')) #int() fucntion expects an integer. Allows for mathematical calculations to be performed with different variables
print(f'Number: {value}')

value = str(input('Enter a number: ')) #str() function converts your input into a string, no matter what it is. Helpful when trying to print 2 different string types together
print(f'Value: {value}')

value = float(input('Enter a number: ')) #float() expects a decimal. Same as int().
print(f'Value: {value}')

