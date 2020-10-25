#Rock-Paper-Scissors Game

a = [
    "Rock",
    "Paper",
    "Scissor",
    "rock",
    "paper",
    "scissor"
]

def calcWinner(user1,user2):
    if (user1 == a[0] or user1 == a[3]) and (user2 == a[0] or user2 == a[3]):
        result = 0
    elif (user1 == a[0] or user1 == a[3]) and (user2 == a[1] or user2 == a[4]):
        result = 2
    elif (user1 == a[0] or user1 == a[3]) and (user2 == a[2] or user2 == a[5]):
        result = 1
    elif (user1 == a[1] or user1 == a[4]) and (user2 == a[1] or user2 == a[4]):
        result = 0
    elif (user1 == a[1] or user1 == a[4]) and (user2 == a[0] or user2 == a[3]):
        result = 1
    elif (user1 == a[1] or user1 == a[4]) and (user2 == a[2] or user2 == a[5]):
        result = 2
    elif (user1 == a[2] or user1 == a[5]) and (user2 == a[1] or user2 == a[4]):
        result = 1
    elif (user1 == a[2] or user1 == a[5]) and (user2 == a[0] or user2 == a[3]):
        result = 2
    elif (user1 == a[2] or user1 == a[5]) and (user2 == a[2] or user2 == a[5]):
        result = 0
    if result == 0:
        print("It's a Tie")
    else:
        print("Player " + str(result) + " Wins")
        

print("*******Rock-Paper-Scissor*******\n")

PlayGame = 1

while PlayGame == 1:
    Player1 = True
    Player2 = True
    while Player1:
        user1 = input("Player 1 Enter your choice >> ")
        if user1 in a:
            Player1 = False
            while Player2:
                user2 = input("Player 2 Enter your choice >> ")
                if user2 in a:
                    Player2 = False
                    calcWinner(user1,user2)
                else:
                    print("Invalid Input")
        else:
            print("Invalid Input")
    PlayGame = int(input("Enter 1 to Play Again and -1 to exit >> "))
