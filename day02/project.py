#this is another simple program; a basic calculator in terminal.
#feel free to copy and expand the code to your liking
print("===========TERMINAL=CALCULATOR===========")
num1 = int(input('Enter Your First Number: ').strip())
num2 = int(input('Enter Your Second Number: ').strip())
opp = input('Enter the Operator You Want to use: [+, -, /, *, //, %, **]')

if opp == '+':
    print(num1 + num2)
elif opp == '-':
    print(num1 - num2)
elif opp == '/':
    print(num1 / num2)
elif opp == '*':
    print(num1 * num2)
elif opp == '//':
    print(num1 // num2)
elif opp == '%':
    print(num1 % num2)
elif opp == '**':
    print(num1 ** num2)
else:
    print('Invalid Operator')
