#day04 simple project; number guesser game.

#TYPE 1
secret = 5
print("======Number Guesser======")
while True:
    answer = int(input("Enter Your Guess: [1-10]"))

    if answer != secret:
        print("Not Quite, try again")
    elif answer == secret:
        print(f"Nice, answer was {secret}")
        break
    
#TYPE 2
print("=====Number Guesser=====")
while True:
    answer = int(input("Enter A Number: [1-10]"))

    if answer > secret:
        print("Too High")
    elif answer < secret:
        print("Too Low")
    else:
        print("Nice")
        break