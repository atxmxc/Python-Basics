#comparisons operators
#here are some comparison operators used in different scenarios, like if statements
'==' #equal to, '=' assigns something so dont confuse the two.
'!=' #not equal to
'>' #greater than
'<' #less than
'>=' #greater than or equal to
'<=' #less than or equal to

#examples
print(10 == 3)
print(23 > 17)
print(21 != 20)
print(34 < 45)

#if, elif and else statements (properly explained)
#if and elif statements work top ---> bottom, meaning that it will scan through the conditions until one of them is met.
#else however, just catches whatever is left, so if none of the conditions are met, it will be filtered to the else statement and execute the code indented.
x = int(input("A Number: "))
if x > 5 and x < 10: #checks if condition is met, then executes it
    print("Ok")
elif x >= 10 and x < 15: #if the first condition wasnt met, then it would check with this statement.
    print("Nice")
elif x >= 15 and x < 20: #then it would check with this statement.
    print("Great")
else:  # if all of them weren't met, then it would get thrown to the else: statement and executed.
    print("Amazing")

#boolean logic
#i've snuck in some boolean logic up in the else, if and elif section but it will be properly explained.
#these boolean factors allow for one or more conditions in a single if statement.
#say for an example you have rankings, you would use the boolean logic to sort who is 3rd, 2nd and 1st.
fourthPlace = 0
thirdPlace = 1
secondPlace = 2
firstPlace = 3
if thirdPlace > fourthPlace and thirdPlace < secondPlace:
    print("He is in third")

if secondPlace > thirdPlace and secondPlace < firstPlace:
    print("He is in second place")

if firstPlace > secondPlace:
    print("He is in first")
