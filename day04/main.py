#while loops
#while loops can be useful in many situations when you need something to run until a condition is met, for example;
count = 0

while count < 5:
    print(count)
    count += 1

#condition must always change otherswise it'll just run for an infinite amount of times.
count = 5

while count > 0:
    print(count)
    x -= 1

#for loops
#these are used when you now how many times to run something before it exits.
for i in range(1, 5):
    print("Hello")
#there are different ways to use the for loop
range(5) # 0 --> 4
range(1, 5) # 1 --> 4
range(1, 10, 2) #1, 3, 5, 7, 9

#break and continue
#these allow you to control the loop flow
while True:
    cmd = input("Type 'exit': ")
    if cmd == 'exit':
        break

for i in range(5):
    if i == 2:
        continue
    print(i)