##Olympics 2020 report part 3
##Adam Avdic,ama193
##Oct.13/2020

##open file
file = open("Olympics2020_medals.csv")

##uneeded header
unneed_header = file.readline()

##greet user
print("Welcome to the 2020 Olympics Results Report!")

print("")

##get user input
chosen_country = input("Which team do you want to know about their medals? "
                        ).lower().strip(" ,.?!")
#accumalate
##for loop to get chosen countries medal count
medal_total = 0
for line in file:

    data = line.split(",")

    if chosen_country in (data[0]).lower():

                          gold_medal = data[1]
                          silver_medal = data[2]
                          bronze_medal = data[3]

                          print("\nTeam " + data[0] + " has won " + str(gold_medal) + " gold, "
                                + str(silver_medal) + " silver, and "
                                + str(bronze_medal) + " bronze medals.")
                          medal_total = (int(gold_medal)+int(silver_medal)+int(bronze_medal))

                          break
                        
##if user inputs country not in file, tell them                              
else:
    print("Sorry that country does not exist in the file.")

##for loop to get other countries medal count
for line in file:
    data = line.split(",")

    gold = data[1]
    silver = data[2]
    bronze = data[3]

    medal_total_new = 0

    medal_total_new = (int(gold)+int(silver)+int(bronze))

##if there's countries with more medals, display them
    if (medal_total_new > medal_total) :
        print("Team " + data[0] + " has won " + str(int(medal_total_new) - int(medal_total))
              + " more medal(s) than your team.")

        
##If user puts in USA, displays message that USA has no other teams had more medals        
medal_total_new = 0
if (medal_total_new < medal_total) :
    print("There is no team winning more medals than your team")


