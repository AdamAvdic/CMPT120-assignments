##A visit to the pikani nation
##Adam Avdic, ama193, 301439186
##Sep.29/2021

#Ask how many people we are serving
reply = int(input("Ok! Welcome to the restaurant. How many people do we have today? => "))

print("\nOk! I'll go around one by one to take your order.\n")

#assign dictionary translations and w/ costs

translation = {"fish":"mamii","fries":"paataakistsi","burger":"pikkiaaksin",
               "coffee":"iitapsiksikimmii","tea":"siksikimmii","water":"aohkii"}

item_prices = {"fish":5.00,"fries":3.00,"burger":4.50,"coffee":1.50,"tea":1.00,
              "water":0.00}

#initialize tallies

fish_tally = 0
fries_tally = 0
burger_tally = 0
coffee_tally = 0
tea_tally = 0
water_tally = 0

#repeat orders w/ user input

for i in range(reply) :

#if statements for user orders
    reply_1 = input(str(i+1) +
                    ". And what would you like to have? (fish/fries/burger) => "
                    ).lower().strip(" .!")
    if reply_1 == "fish" :
        print("So that's one " + translation[reply_1])
        fish_tally += 1
    elif reply_1 =="fries" :
        print("So that's one " + translation[reply_1])
        fries_tally += 1
    elif reply_1 == "burger" :
        print("So that's one " + translation[reply_1])
        burger_tally += 1
    else:
        print("Sorry we don't have that...")

    reply_2 = input("What would you like to drink? (coffee/tea/water)=> ").lower().strip(" .!")
    if reply_2 == "coffee" :
        print("and one " + translation[reply_2] + ".")
        coffee_tally += 1
    elif reply_2 == "tea" :
        print("and one " + translation[reply_2] + ".")
        tea_tally += 1
    elif reply_2 == "water" :
        print("and one " + translation[reply_2] + ".")
        water_tally += 1
    else :
        print("Sorry we don't have that, here's a water.")
        water_tally += 1

#assign another dictionary for tallies

food_with_tallys = {"fish":fish_tally,"fries":fries_tally,
                    "burger":burger_tally, "coffee":coffee_tally,"tea" : tea_tally ,
                    "water" : water_tally}

#repeat back orders

print("\nOk, here are the orders I have")

#for loop for printing back orders
for orders in food_with_tallys :
    if food_with_tallys[orders] > 0 :
        print(str(food_with_tallys[orders]), translation[orders]  +  "(" + orders + ")")

#for loop for giving final price
#accumalate pattern
total = 0
for item in food_with_tallys :
    price = food_with_tallys[item]*item_prices[item]
    total += price

#print final price w/ 2 decimal points

print("\nAnd your total is $" + "{:.2f}".format(total) + ".")

