# normal function
def message():
    print("Hello to the new world")

message()

# function with parameter

def message(a):
    print("Hello I got a message for you :"+a)

message("You are very good")

#function with parameter and return type
def add(a,b):
    return a+b

print(add(5,6))

#Function as parameter

def square(z):
    return z*z

print(square(add(6,7)))
