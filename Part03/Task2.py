userInput = int(input("Enter a number >> "))

a = []

for i in range(1, userInput+1):
    if userInput % i == 0:
        a.append(i)

print(" List of numbers that are divisible by " + str(userInput) + " are : " + str(a))