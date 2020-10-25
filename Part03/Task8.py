#Hangman Game
import random

listOfWords = [
    "APPLE", "BILBO", "CHORUSED", "DISIMAGINE",
    "ENSURING", "FORMALISING", "GLITCHES", "HARMINE",
    "INDENTATION", "JACKED", "KALPACS", "LAUNDRY", 
    "MASKED", "NETTED", "OXFORD", "PARODY", "QUOTIENTS",
    "RACERS", "SADNESS", "THYREOID", "UNDUE", "VENT", 
    "WEDGED", "XERIC", "YOUTHHOOD", "ZIFFS"
]

def pickRandomFromList():
    return listOfWords[random.randint(0,25)]

def generateGuessString(word, guessedCharacters):
    string = ""
    for char in word:
        found = False
        for elem in guessedCharacters:
            if elem == char:
                found = True
                break
        if found:
            string += char
        else:
            string += '_'
        string += ' '
    return string

PlayGame = True
while PlayGame:
    print("********Hangman********\n")
    word = pickRandomFromList()
    isNumberGuessed = False
    turns = 9
    guessedCharacters = []
    guessString = ""
    guessString = generateGuessString(word, guessedCharacters)
    print(guessString)
    while (isNumberGuessed == False) and turns != 0:
        if '_' in guessString:
            print("You are left with " + str(turns) + " turns")
            userInput = input("Guess a letter >> ")[:1]
            if userInput in word:
                guessedCharacters.append(userInput)
            else:
                print("Wrong Character")
            turns -= 1
            guessString = generateGuessString(word, guessedCharacters)
            print(guessString)
        else:
            isNumberGuessed = True
    if isNumberGuessed:
        print("YOU GUESSED IT!")
    else:
        print("\n-----GAME OVER-----")
        print("\nThe Words was : " + word)
    temp = int(input("Press 1 to play again and 0 to exit : "))
    if(temp == 0):
        PlayGame = False