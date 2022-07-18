# Title: Movie Similarity Score Calculator
# Author:
# Date:

# Description: Finds out how similar two people are 
# by comparing their lists of favourite movies.

# 1. Get the favourite movies for each person
victor_favourite_movies = ["Big Hero 6", "Wreck-It Ralph", "Frozen"]
vincent_favourite_movies = ["Wreck-It Ralph", "Big Hero 6", "Wall-E"]

# 2. Initialize a common interest counter

common_interest_counter = 0


# 3. Go through all the favourite movies of the first person

for movie in victor_favourite_movies:
    
    #   3a. If that movie is also in the other person's list
    if movie in vincent_favourite_movies:
#       Add to the common interest counter
        common_interest_counter += 1
        

# 4. Print the common interest counter to show the similarity score

print("Similarity score: " + str(common_interest_counter))
