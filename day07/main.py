#dictionaries
#easier way to store data instead of using lists
names = ["Andy", 14]
#goes to
person = {
    "name": "Andy",
    "age": 14
}

#creating dictionaries is relatively simple, you just need to know what you will store in it
#example
car = {
    "make": "Honda Civic",
    "year": 2014,
    "color": "Silver",
    "BHP": 103
}
#accessing values
#you can access values from a dictionary but calling the name of the value
print(car["make"])
print(car["year"])
#however, this is only useful if you are sure you know all of the keys, if you dont, use car.get[] in my case
print(car.get("BHP"))
print(car.get("age"))

#adding and removing values from a dictionary
#relatively simple, all you need to do us call the name of the dictionary, then write the name of the value inside it; it will either upfate or make a new row

car["Mileage"] = 34521
car["Reliable"] = "very"

#removing values is the same except you just need to specifiy the name of the value
del car["Reliable"]
#or
car.pop("Reliable", None)

#looping through dictionaries
# for make in car:
#     print(make, car['make'])

#or

for make, value in car.items():
    print(make, value)