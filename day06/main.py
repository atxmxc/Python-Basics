#lists
#lists allow you to store multiple pieces of data in a single variable. They also allow you to filter them to pick out what you need,
numbers = [1, 2, 3, 4, 5]
names = ['andy', 'john', 'smithh', 'wesson']

#indexing
#this allows you to pick out a 1 or more pieces of data from that variable
print(numbers[0])
print(names[3])
#indexing can also go into the negatives
print(numbers[-2])
print(names[-1])

#adding & removing
#you can add and remove data using the .append() and .remove() function
names.append("Oliver")
numbers.append(14)

names.remove('andy')
numbers.remove(3)

#looping through lists
#you can also loop through lists, outputing what is stored inside it
for name in names:
    print(name)
