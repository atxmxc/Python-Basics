#day05 project; a bit more advanced calculators with functions
def get_num(prompt):
    return int(input(prompt).strip())

def calculate(a, b, opp):
    if opp == '+':
        return a + b
    elif opp == '-':
        return a - b
    elif opp == '/':
        return a / b
    elif opp == '*':
        return a * b
    elif opp == '**':
        return a ** b
    elif opp == '//':
        return a // b
    elif opp == '%':
        return a % b
    else:
        return None

print("=======Calculator=======")
num1 = get_num("Number: ")
num2 = get_num("Number: ")
operator = input("Enter Operator: ")

result = calculate(num1, num2, operator)

if result is not None:
    print(f'Answer: {result}')
else:
    print('Invalid')
