##Adam Avdic,ama193,301439186
##SFU wildlife game
##Sep.26/2021

##import random

import random

##make sure the game plays 3 times, for loop w/ range

for i in range (3) :

##accepts both upper and lowercase user input and ignores blank spaces

##assign lists
    
    reply = input("Where are you ? (ASB,AQ) -> ").lower().strip(" .! ")

    locat = ["asb", "aq"]

    random_area = random.choice(locat)

    final_location = random_area

    poss_ans = ["bear", "friend", "professor","coyote"]

    random_ans = random.choice(poss_ans)

    bear_prof_friend = random_ans

    greetings = ["YOU AVOID", "YOU GREET"]

    random_greeting = random.choice(greetings)

    greeting_1 = random_greeting
    
##AI makes random decision
    
    print("There is a " + random_ans + " in the " + random_area)


##if/elif/else for game logic


    if reply in final_location :
        
        reply_1 = input("You are having an interaction! Press Enter to see what you do! ")
        print(random_greeting)
        
        if greeting_1 == "YOU AVOID" and random_ans == "bear" :
            print("YOU SURVIVE")

        elif greeting_1 == "YOU GREET" and random_ans == "bear" :
            print("You got eaten!")

        elif greeting_1 == "YOU GREET" and random_ans == "coyote" :
            print("You got eaten!")

        elif greeting_1 == "YOU AVOID" and random_ans == "coyote" :
            print("YOU SURVIVE")

        elif greeting_1 == "YOU AVOID" and random_ans == "professor" :
            print("YOU SURVIVE")

        elif greeting_1 == "YOU GREET" and random_ans == "professor" :
            print("YOU SURVIVE")

        elif greeting_1 == "YOU AVOID" and random_ans == "friend" :
            print("UH OH!")

        elif greeting_1 == "YOU GREET" and random_ans == "friend" :
            print("YOU SURVIVE")

    else:
        print("No interactions for now...")



    


        



    

    
    
    

        
