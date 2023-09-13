import random

startGame = False

userScore = 0
computerScore = 0

options = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors")
print("Enter the choice: (1/2)")
print("1. Start game")
print("2. Exit")
userMenuSelection = int(input("Selection: "))


def gameStart():
    print("Game started!")
    while True:
        result = gameRound()
        if result == "You won!" or result == "Computer won":
            print("================")
            print("Your score: ", userScore)
            print("Computer's score: ", computerScore)
            print(result)
            break


def gameRound():
    global userScore
    global computerScore

    print("================")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    userChoice = int(input("Enter your move (1/2/3): "))

    if userChoice > 3:
        return

    computerChoice = random.randint(1, 3)
    print("Your move:", options[userChoice - 1])
    print("Computer's move:", options[computerChoice - 1])

    if (
        (userChoice == 1 and computerChoice == 3)
        or (userChoice == 2 and computerChoice == 1)
        or (userChoice == 3 and computerChoice == 2)
    ):
        print("You scored a point!")
        userScore += 1
    elif userChoice != computerChoice:
        print("Computer got a point!")
        computerScore += 1
    else:
        print("It's a tie")

    if userScore == 5 or computerScore == 5:
        if userScore > computerScore:
            return "You won!"
        else:
            return "Computer won"


if userMenuSelection == 1:
    gameStart()

else:
    print("Exiting game!")