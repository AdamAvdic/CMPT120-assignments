import turtle
import random

colours = ["blue","green","red"]

adam = turtle.Turtle()

length = input("What is the length of the largest square? ==> ")

random_colours = random.choice(colours)

square_color = random_colours



def draw_square_special(length):
    adam.begin_fill()
    adam.color(square_color)
    adam.end_fill()
    for i in range(4):
        adam.forward(float(length))
        adam.left(90)
        length -= 5


length = 200

for i in range (10):
    draw_square_special(float(length))
    length -= 20
    
    
