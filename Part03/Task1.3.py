#user inputing the number we want to comapre
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

userInput = int(input("Enter the number to be compared >> ")) 

for elem in a:
    if elem < userInput:
        b.append(elem)

print(b)