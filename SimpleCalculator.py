# define the function needed: add, sub, mul, div

def add(a, b):
    ans = a + b
    print(str(a) + " + " + str(b) + " = " + str(ans) + "\n")

def sub(a, b):
    ans = a - b
    print(str(a) + " + " + str(b) + " = " + str(ans) + "\n")

def mul(a, b):
    ans = a * b
    print(str(a) + " * " + str(b) + " = " + str(ans) + "\n")

def div(a, b):
    ans = a / b
    print(str(a) + " / " + str(b) + " = " + str(ans) + "\n")

# from unittest import FunctionTestCase
# print options to the User
# ask for values
# call the Functions
# while loop to continue the program until the user wants to exit

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("%. Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        print("Addition")
        a = int(input("Enter first Number: "))
        b = int(input("Enter second Number: "))
        add(a, b)

    elif choice == "2":
        print("Subtraction")
        a = int(input("Enter first Number: "))
        b = int(input("Enter second Number: "))
        sub(a, b)

    elif choice == "3":
        print("Multiplication")
        a = int(input("Enter first Number: "))
        b = int(input("Enter second Number: "))
        mul(a, b)

    elif choice == "4":
        print("Division")
        a = int(input("Enter first Number: "))
        b = int(input("Enter second Number: "))
        div(a, b)

    elif choice == "5":
        print("Program Ended")
        quit()