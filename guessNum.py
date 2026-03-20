# Genarate the random num
# Loop
# Ask the user to make guess
# If not a valid num
  #print an error
# If number < guess
  # print too low
# If number > guess
   # print too high
# Eles
# Print well done

import random
numToGuess = random.randint(1, 100)

while True:
  try:
    userInput = input('Guess the number between 1 and 100: ')
    guess = int(userInput)
 
    if guess < numToGuess:
        print("Too Low")
    elif guess > numToGuess:
        print("Too High")
    else:
        print("Congratulations")
        break
  except ValueError:
    print("Please enter valid number")