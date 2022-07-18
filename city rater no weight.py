# City Rater
# Author: Adam Avdic
# Date: sep29/2021

# Description: Asks the user a few questions about a city,
# each require them to provide a rating (1 to 5),
# then calculate the average score

# Greet the user and ask for a city to rate
city = input("Hello! Which city would you want to rate? ").strip(" !.?")

# Make a list of questions
factors = ["transportation", "air quality", "cost of living", "safety"]

# Initialize the score
total_score = 0

# Go through each question, get rating, and add it up
for factor in factors:
    rating = int(input("What is your rating regarding " + factor + "? (from 1-5"))
    total_score += rating
    
# Calculate the final score by taking the average of the total
#   For example, if there are 2 questions and the ratings are 4 & 3,
#   then the final score will be (4+3)/2 = 3.5
number_of_questions = len(factors)

print("The average rating for " + city + "is " + "{:.2f}".format(total_score/number_of_questions))
