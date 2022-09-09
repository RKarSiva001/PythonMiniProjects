# import the module: random
# ask user if they want to generate a password or not
# if yes,
#       ask for password length 
#       generate and print password
# if no, 
#       exit the program

import string
import random

lowerCharacters = list(string.ascii_lowercase)
upperCharacters = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list("!@#$%^&*()")

"""
print(string.ascii_lowercase, string.ascii_uppercase, string.ascii_letters, string.digits, sep="\n")
"""
def generatePassword():
    passLen = int(input("Enter the password length : "))
    
    password = []
    
    for i in range(passLen):
        if i == 0:
            password.append(random.choice(upperCharacters))
        elif i >= 1 and i <= (passLen-4):
            password.append(random.choice(lowerCharacters))
        elif i >= 1 and i <= (passLen-3):
            password.append(random.choice(numbers))
        elif i == (passLen-2):
            password.append(random.choice(symbols))
        else:
            password.append(random.choice(lowerCharacters))
    
    # random.shuffle(password)
    
    password = "".join(password)
    
    print(password)

ch = input("Want to generate a password : ")

if ch.lower() == "y":
    generatePassword()
elif ch.lower() == "n":
    print("Program ended.")
else:
    print("invalid input. Please, try 'y' or 'n'")
    quit()