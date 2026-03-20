# Ask the user to make a choise
# If choise is not valid
# print an error
# Let the computer to make a choise
# Print choises
# Determine the winner
# Ask the user if they want to continue
# If not
# Terminate
import random

emojis = {"r": "🪨", "p": "✂️", "s": "📃"}
choises = ("r", "p", "s")

while True:

    user_choise = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choise not in choises:
        print("Invalid Choise")

    cumputerChoise = random.choice(choises)

    print(f"You chose {emojis[user_choise]}")
    print(f"Computer chose {emojis[cumputerChoise]}")

    if user_choise == cumputerChoise:
        print("Tie")
    elif (
        (user_choise == "r" and cumputerChoise == "s")
        or (user_choise == "s" and cumputerChoise == "p")
        or (user_choise == "p" and cumputerChoise == "r")
    ):
        print("You win !")
    else:
        print("You Lose!!")

    shouldContinue = input("Continu? (y/n): ").lower()
    if shouldContinue == "n":
        break
