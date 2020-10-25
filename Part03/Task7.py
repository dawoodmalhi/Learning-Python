import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation    

def passLength():
    return int(input("Enter the Length of the Password >> "))

def passStrength():
    return int(input("Enter Strength(Weak : 1, medium : 2, Strong : 3) >> "))

length = passLength()
strength = passStrength()
password = ""

if strength == 1:
    for i in range(length):
        password += LETTERS[random.randint(0,51)]

elif strength == 2:
    for i in range(length):
        choice = random.randint(1,2)
        if choice == 1:
            password += LETTERS[random.randint(0,51)]
        elif choice == 2:
            password += NUMBERS[random.randint(0,9)]

elif strength == 3:
    for i in range(length):
        choice = random.randint(1,3)
        if choice == 1:
            password += LETTERS[random.randint(0,51)]
        elif choice == 2:
            password += NUMBERS[random.randint(0,9)]
        elif choice == 3:
            password += PUNCTUATION[random.randint(0,31)]

print("Password generated is below")
print(password)

