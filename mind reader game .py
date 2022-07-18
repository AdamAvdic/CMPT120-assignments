# Mind Reader Game
# Author
# Date

# Description: Second player guesses one of the first
# player's words

# Introduce the game

import random

print("Welcome to Mind Reader!")

words = ["cat", "dog", "apple"]

##assign score

score = 0

for i in range(3):
    
    # Ask 1st player to enter 3 words associated with a given word
    selected_word = random.choice(words)
    print("Player 1, enter 3 words you think of when I say " + selected_word + "?")

    # Get the 3 words
    first_word = input("First word: ")
    second_word = input("Second word: ")
    third_word = input("Third word: ")

    # Clear the screen
    print(100*"\n")

    # Ask the 2nd player to guess an associated word
    print("Player 2, what word do you think Player 1 associates with " + selected_word + "?")
    guess = input().lower().strip(" .!")
    
    # Check if they match and tell them if they win

    if guess in [first_word, second_word, third_word] :
        print("Congrats you have won!")
        score = score + 10

    else :
        print("Sorry there is no match for " + selected_word + "?")


print("Your score is " + str(score))
 
