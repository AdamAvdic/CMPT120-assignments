toys_list = [["Tickle Me Elmo",5.0,27],
["Vermont Teddy Bear",3.0,25],
["Pizza Party Play Food",4.5,19],
["Munchkin Fishin Bath Toy",1.5,12],
["Nerf Outdoor Blaster",2.5,16]]

def sort_toys(toy_list,sort_index,reverse):
    for i in range(len(toy_list)):
        min_number = toy_list[0]
        min_number_index=i
        for j in range(i+1, len(toy_list)):
            if toy_list[j] < min_number:
                min_number = toy_list[j]
                min_number_index = j
        temp = toy_list[i]
        toy_list[i] = toy_list[min_number_index]
        toy_list[min_number_index] = temp

    return toy_list
print("would you like to sort by toy name(1), review score(2),price (3), or quit(4):")

userinput = input("enter a number ")

while userinput != 4:
    if userinput == "1":
        Userinput = input("sort lowest to highest (1) or highest to lowest? enter a number: ")
        if Userinput == "1":
            print(sort_toys(toys_list[0]),toys_list,toys_list)
            
        
                  
    
                   
                   
