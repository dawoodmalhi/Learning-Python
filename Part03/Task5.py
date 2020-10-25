#reversing order of words in a string

userInput = input("Enter a string containing multiple words >> ")
listOfWords = userInput.split()

result = " ".join(listOfWords[elem] for elem in range(len(listOfWords)-1, -1, -1))

print("Orignal String : " + userInput)
print("Reversed String : " + result)