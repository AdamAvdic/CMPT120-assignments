#https://www.tutorialspoint.com/generating-random-number-list-in-python
import random
from functools import reduce

A = [1,]

def divby3(x):
    return int(x)%3 == 0
def list_of_1(x):
    return x * userinput
def add(x,y):
    return x + y  
userinput = int(input("type an integer number >8 and <13 -->"))
randomlist = []
for i in range(0,userinput):
    n = random.randint(1,21)
    alist = randomlist.append(n)

final_list = alist

print("list with random numbers ", final_list)



##filteredlist = list(filter(divby3,final_list))
##convertedlist= list(map(int,final_list))
##
##print(reduce(add,convertedlist))


def version_map_filter_reduce(lst):
    
    filteredlist = filter(divby3,lst)
    convertedlist = map(int,lst)
    print(reduce(add, convertedlist))

version_map_filter_reduce(final_list)


