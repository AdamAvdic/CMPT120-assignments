## My signed turtled work of art
## Adam Avdic, ama193, 3014186
## 10/16/2021
##import turtle,random and assign name
import turtle
import random
adam = turtle.Turtle()

# #make background w/ loop
def square():
  for x in range(4):
    adam.forward(350)
    adam.left(90)

##make background 
adam.penup()
adam.goto(-180,-170)
adam.pendown()
adam.color("black","black")
adam.begin_fill()
square()
adam.end_fill()

##pac-man drawing
def pacman():
  adam.penup()
  adam.goto(-30,-65)
  adam.pendown()
  adam.color("white","yellow")
  adam.begin_fill()
  adam.circle(80)
  adam.end_fill()

##insert pac-man
adam.penup()
adam.goto(0,-50)
adam.pendown
pacman()

##pac-man mouth
def pacmanmouth():
  adam.color("black","black")
  adam.begin_fill()
  adam.right(90)
  adam.forward(100)
  adam.right(120)
  adam.forward(100)
  adam.end_fill()

##insert pacman mouth
adam.penup()
adam.goto(50,70)
adam.pendown()
pacmanmouth()

##make pacman-candy
def pacman_ball(x,y):
  adam.penup()
  adam.goto(50+x,0+y)
  adam.pendown()
  adam.color("white","white")
  adam.begin_fill()
  adam.circle(10)
  adam.end_fill()

##insert pac-man candy 
pacman_ball(20,30)
pacman_ball(60,30)
pacman_ball(100,30)

##pacman eye that changes color from random 
random_colors = ["red", "black", "orange"]
random_colors_choice = random.choice(random_colors)
eye_color = random_colors_choice
def pacmaneye():
  adam.color(eye_color)
  adam.begin_fill()
  adam.circle(5)
  adam.end_fill()

##insert pacman eye
adam.penup()
adam.goto(10,70)
adam.pendown()
pacmaneye()

##first letter A
def letter_A_1():
  adam.color("white")
  adam.right(90)
  adam.forward(40)
  adam.right(120)
  adam.forward(20)
  adam.right(120)
  adam.forward(20)
  adam.right(180)
  adam.forward(20)
  adam.right(60)
  adam.forward(20)

##insert first letter A
adam.penup()
adam.goto(-120,-120)
adam.pendown()
letter_A_1()

##second letter A
def letter_A_2():
  adam.color("white")
  adam.right(240)
  adam.forward(40)
  adam.right(120)
  adam.forward(20)
  adam.right(120)
  adam.forward(20)
  adam.right(180)
  adam.forward(20)
  adam.right(60)
  adam.forward(20)

##insert second letter A
adam.penup()
adam.goto(-60,-120)
adam.pendown()
letter_A_2() 

##number 6 w/ for loop 
def number_6():
  adam.color("white")
  adam.right(-150)
  adam.forward(40)
  adam.right(90)
  adam.forward(10)
  adam.right(180)
  adam.forward(10)
  adam.left(90)
  adam.forward(40)
  adam.left(90)
  for x in range(4):
    adam.forward(20)
    adam.left(90)

##insert number 6
adam.penup()
adam.goto(0,-120)
adam.pendown()
number_6()

##make pinky w/ for-loop
def pinky():
    adam.left(90)
    adam.forward(60)
    adam.circle(20,180)
    adam.forward(60)
    for x in range(11):
        adam.left(160)
        adam.forward(10)
        adam.right(160)
        adam.forward(10)

##insert pinky
adam.penup()
adam.goto(120,-90)
adam.pendown()
adam.color("white","pink")
adam.begin_fill()
pinky()
adam.end_fill()

##make pinky eyes
def pinkyeyes():
  adam.color("white","white")
  adam.begin_fill()
  adam.circle(2)
  adam.end_fill()

##insert first pinky eye
adam.penup()
adam.goto(90,-30)
adam.pendown()
pinkyeyes()

## insert second pinky eye
adam.penup()
adam.goto(110,-30)
adam.pendown()
pinkyeyes()



