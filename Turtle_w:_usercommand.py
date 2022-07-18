import turtle
alex.turtle.Turtle()

keep_looping = True

while keep_lopping:
    
    command = input("What shall I do? f/s/stop: ").lower()

    if command == "stop":
        keep_looping = False
    elif command == "f":
        alex.forward(10)
    elif command == "s":
        alex.stamp()
    else:
        print("command not recognized")

print("end of program")
    
