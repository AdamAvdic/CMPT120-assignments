# Title: Most Similar Person Finder
# Author:
# Date:

# Read from a data file containing the information from multiple people
# and find the one most similar to the first entry

# Open the file, remove the header line if it exists
file = open("favourites-survey.csv")
header = file.readline()

# Read the first entry and get the list of favourites
# Assuming that this entry represents yourself
my_favorites = file.readline().strip().split(",")

# Initialize variables for top friend and similiarity score
top_friend = ""
top_score = 0

# Go through each line of the remaining file, each is an entry
for line in file:
    
  # Get their favourites
  their_favourites = line.strip().split(",")
  their_name = their_favourites[1]
  
  # Initialize common interest counter with each person
  common_interest_counter = 0
  
  # For each of my favourites see if it's in theirs too
  for fave in my_favorites:
      if fave in their_favourites:
          common_interest_counter += 1
          
  # If the score is higher than the current top score, update
  if common_interest_counter > top_score:
      top_friend = their_name
      top_score = common_interest_counter

# Print the most similar person
print(top_friend + " similarity score: " + str(top_score))
