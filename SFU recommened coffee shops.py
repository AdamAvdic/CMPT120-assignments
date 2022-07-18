# Title: Getting Coffee at SFU
# Author: Adam Avdic
# Date: 
# Description: This program gets 5 users to find out what their faviourite
#  cafe on campus is. It prints out the number of people who likes Starbucks,
#  Time Hortons, or Renaissance.

# Initialize tallies
starbucks_tally = 0
timmies_tally = 0
renaissance_tally = 0

# repeat the below 5 times

for i in range(5) :
    
    # Ask the user what their favourite cafe is
    favourite_cafe = input(str(i+1) + ". What's your favourite cafe? ").lower().strip(" .!")

    # If they say starbucks, add one to the starbucks tally
    if favourite_cafe == "starbucks" :
        starbucks_tally = starbucks_tally + 1


    # If the say tim hortons, add one to the timmys tally
    if favourite_cafe == "tim hortons":
                           timmies_tally += 1 


    # If they say renaissance, add one to the renaissance tally
    if favourite_cafe == "renaissance" :
                           renaissance_tally += 1
        


# In the end, print out the tallies
print("Starbucks: " + str(starbucks_tally/5*100)+ "%")
print("Tim hortons: " + str(timmies_tally/5*100)+ "%")
print("Renaissance: " + str(renaissance_tally/5*100) + "%")


    
