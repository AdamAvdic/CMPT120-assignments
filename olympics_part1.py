##Olympics 2020 report part 1
##Adam Avdic, ama193
##Oct.10/2021

##open file and remove header
file = open("Olympics2020_medals.csv")
file.readline()

##print greeting message
print("Welcome to the Olympics 2020 Results Report!")

##accumalation 
total_medals_won = 0
country_medal_won = 0

##assign variables, easier to read
##for loop to get total number of medals won
for line in file:
    data = line.strip().split(",")
    country = data[0]
    gold_medal = data[1]
    silver_medal = data[2]
    bronze_medal = data[3]
    
    country_name = (int(gold_medal)
                    + int(silver_medal)
                    + int(bronze_medal))
    total_medals_won += country_name
    
##print out total and print out total number of medals won by each team
print("\nA total of " + str(total_medals_won) + " were given out in the Olympics 2020")
print("\nHere are the total number of medals won by each team: ")

##file.seek(0) to reset pointer
##remove header again
file.seek(0)
header = file.readline()

##for loop once again to get total medals
for line in file:
    data = line.strip().split(",")
    country = data[0]
    gold_medal = data[1]
    silver_medal = data[2]
    bronze_medal = data[3]

    country_medals_won = int(gold_medal)+ int(silver_medal)+ int(bronze_medal)

##Put total in a percentage of total medals won by each country
    percentage = ("{:.3f}%".format(country_medals_won/total_medals_won*100))
    
##print out total medals won by each country including percent
    print(country + ": " + str(country_medals_won) + " " + "(" + percentage+ ")")

    
