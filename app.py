import random

myScore = 0
computerScore = 0
validOptions = ["rock", "paper", "scissors"]

while True:
    myInput = input("Rock, Paper, or Scissors? ")
    myInput = myInput.lower()

    if myInput not in validOptions:
        print("Invalid option. Please choose rock, paper, or scissors.")
        continue

    computerInput = random.choice(validOptions)

    print("Computer chose:", computerInput)
    print("You chose:", myInput)

    if myInput == computerInput:
        print("Tie!")
    elif (myInput == "rock" and computerInput == "scissors") or (myInput == "paper" and computerInput == "rock") or (myInput == "scissors" and computerInput == "paper"):
        print("You win!")
        myScore += 1
    else:
        print("You lose!")
        computerScore += 1

    print("Computer score:", computerScore, "Your score:", myScore)

    playAgain = input("Do you want to play again? (yes/no) ")
    if playAgain.lower() == "no":
        break

print("Thanks for playing!")