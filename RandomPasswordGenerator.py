# import the module: random
# ask user if they want to generate a password or not
# if yes,
#       ask for password length 
#       generate and print password
# if no, 
#       exit the program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
"""
def generatePassword(length):
passLen = int(input("Enter the password length : "))
password = ""
for i in range(passLen):
    password += random.choice(characters)
print("Password : ", password)    
"""
print(string.ascii_lowercase, string.ascii_uppercase, string.ascii_letters, string.digits, sep="\n")

"""
def generatePassword():
    passLen = int(input("Enter the password length : "))
    
    random.shuffle(characters)
    
    password = []
    
    for i in range(passLen):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "".join(password)
    
    print(password)

ch = input("Want to generate a password : ")

if ch.lower() == "yes":
    generatePassword()
elif ch.lower() == "no":
    print("Program ended.")
else:
    print("invalid input. Please, try 'yes' or 'no'")
    quit()
"""