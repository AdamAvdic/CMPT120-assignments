#import turtle package 

import turtle

#create our turtle

adam = turtle.Turtle()

def drawACookie(x,y):
    #draw cookie outside

    adam.penup()
    adam.goto(-5 + x,-30 + y)
    adam.pendown()
    adam.circle(30)
    adam.penup()

    adam.goto (0+x,0+y)
    adam.stamp()

    adam.goto(-10+x,10+y)
    adam.stamp()

    adam.goto(-10+x,-10+y)
    adam.stamp()

    adam.goto(10+x,-10+y)
    adam.stamp()

    adam.goto(10+x,10+y)
    adam.stamp()

#Call (invoke) a function
drawACookie(0,0)

drawACookie(50,50)





