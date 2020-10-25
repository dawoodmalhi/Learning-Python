#finding if a string is palindrome or not

userInput = input("Enter a String >> ")

reverseString = userInput[::-1]

if userInput == reverseString:
    print("Given String is Palindrome")
else:
    print("Given String is not Palindrome")