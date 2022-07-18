# Titel: Favourite Pets
# Author: 
# Date:

# Description: Read the data file containing survey answers
# and find out the favourites of the class by counting how many
# times each item was voted for

# Open the data file
file = open("favourites-survey.csv")


# Read the first (header) line in the file
unneed_header = file.readline()

# Read the first real data line

# Initialize the tallies using the accumulator pattern

cat_tallies = 0
dog_tallies = 0


# Loop through the lines
for data in file:
    data_list = data.split(",")
    fav_pet = data_list[3].lower().strip(" .!?")

    if fav_pet == "cat":
        cat_tallies += 1
    elif fav_pet == "dog":
        dog_tallies += 1

# Print results

print("cat people: " + str(cat_tallies))
print("Dog people: " + str(dog_tallies))
