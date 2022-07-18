#coffee bot

#greet user and ask Q
coffee = input("Hi,i am coffeebot, would you like cream?-> ")

#possible answers
if coffee == "Yes" or coffee == "yes" :
    print("Here's your coffee with cream")

elif coffee == "No" or coffee == "no" :
    print("Here's your coffee, no cream")

else:
    print("Sorry, I dont know what " + coffee + " means")
