#lists
fruits = ['apple', 'grapefruit', 'tomato']
fruits.append('torange')

print("Printing a list of fruits", fruits)

#numbers
numerics = (1, 4, 6, 5)
print(numerics[2])

#sets
set = {1,1,1,1,1, 2,2, 3, 3, 5,4,6}
print(set)

#dictionary
dict = {'course': 'ai for devs', 'year': 2025}
print(dict)

#functions
def isOdd(number) :
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")


#for loop
for i in range(10):
    isOdd(i)
    
#while loop
iterations = 0
while iterations < 10:
    isOdd(iterations)
    iterations += 1


#standard arguments functions
def greeting(name = "some person..."):
   return f"Hello, {name}!"

print(greeting())
print(greeting("André"))


#file manipulation
FILENAME = "./testFile_fundamentals.txt"
with open(FILENAME, 'w') as file:
    file.write(greeting("'File Reader'"))

with open(FILENAME, 'r') as file:
    contents = file.read()
    print(contents)

import math
print(math.sqrt(16))

from my_module import sum
print (sum(3, 4))

#list comprehension
squares = [x ** 2 for x in range(10)]
print(squares)


#decorators
def decorator_greeting(func):
    def wrapper(*args, **kwargs):
        print(f"Now we will say hello to: {args[0]}")
        return func(*args, **kwargs)
    return wrapper

@decorator_greeting
def hello(name):
    print(f"Hello, {name}!")

hello("Vargas")


class ClassRoom:
    def __enter__(self):
        print("Entering the classroom.")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the classroom.")
    
with ClassRoom():
    print("Hey! I'm studying here")