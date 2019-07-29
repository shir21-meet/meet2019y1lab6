import turtle
turtle.goto(0,0)

def up():
    print("you pressed the up key.")
def w():
    turtle.forward(100)

turtle.onkey(up, "Up")
turtle.onkey(w, 'w')
turtle.goto(0,0)
turtle.listen()

    
    

