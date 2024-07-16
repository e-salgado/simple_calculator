# A simple calculator program

# create operation functions
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y

# Display menu choices to user
print("Choose an Operation")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

# Validate input and determine which operation to perform, ask user if they want to enter another equation
while True:
    # get user input
    choice = input("Enter Choice 1/2/3/4: ")

    # check choice
    if choice == "1":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, " + ", num2, " = ", add(num1, num2))
    elif choice == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1, " - ", num2, " = ", sub(num1, num2))
