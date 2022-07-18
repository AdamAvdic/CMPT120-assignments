#Chatbot with personality
#Adam Avdic, ama193, 301439186
#Sep.16/2021
#


#code asks question w/ print and input + if statement

reply = input("Hi, what is your name? ->").lower()

print("\nHi, nice to meet you " + reply)
if reply == "adam" : 
    print("\nMy name is Adam too!")


#one if/elif statement w/ no else

print("\nDo you prefer apples or oranges?")

reply_1 = input().lower()

if reply_1 == "apples" :
    print("Awesome, I like apples too!")

elif reply_1 == "oranges" :
    print("Oh, I do not like oranges...")

#one if/elif/else statement

print("\nHow is your day going?")

reply_2 = input().lower()

if reply_2 == "good" or reply_2 == "excellent" or reply_2 == "fabulous":

    print("glad to hear")

elif reply_2 == "bad" or reply_2 == "slow":
    print("sorry to hear:(")
else:
    print("Oh.... okay?!")

print("\nHave a good day " + reply)

