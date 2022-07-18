##Olympics 2020 report part 2
##Adam Avdic, ama193
##Oct.10 2021

##open file
file = open("Olympics2020_medals.csv")

##remove header
unneed_header = file.readline()

##accumalate line reader
country_line = 0

##Print welcome message
##Input user on which teamt they would like the report on 
print("Welcome to the 2020 Olympics Results Report!")

print("")

chosen_country = input("Which team do you want to know about their medals? "
                        ).lower().strip(" ,.?!")

##set invalid country to False incase user puts a country not in file

invalid_country = False


##For loop to get info on amount of medals won by each country
for line in file:
    data = line.strip().split(",")
    country_line += 1
    country = data[0].lower()
    gold_medal = data[1]
    silver_medal = data[2]
    bronze_medal = data[3]
    
##if statement proving user input matches a country on file
    if chosen_country == country:
        invalid_country = True
        
        print("\nTeam",data[0], "has won", gold_medal, "gold,",
              silver_medal, "silver,", bronze_medal,"bronze.")

        print("\nThe team is at line ",str(country_line),
              "in the file excluding the header line")
        
##if statement outside loop proving country not in file
if not invalid_country:
    
    print("Sorry, that country doesn't exist in the system.")



