# Guess a number game
# Author:
# Date:

# Description: A game where the bot chooses a random number
# and the user has to guess the number

import random

# Bot chooses a secret random number between 1-100
secret_number = random.choice(range(1, 101))

# User guesses a number
guess = int(input("Please guess a number between 1-100! "))

#initialize another control variable
guesses_left = 9

# Keep looping until the user guesses the number
# or reaches a maximum number of guesses
while guess != secret_number and guesses_left > 0:
    # Tell the user whether the secret number is higher or lower
    if guess < secret_number:
        guess = int(input("Higher! Try again: "))
    else:
        guess = int(input("Lower! Try again: "))

    guesses_left -= 1

if guess == secret_number:

        
# Output the final result
    print("You've got it! The number is " + str(secret_number))
else:
    print("You have run out of guesses.")
