
import turtle
import random

#the screen
sc=turtle.Screen()
sc.tracer(1,0)
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

 #Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")
turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos() 
    pos_list.append(snake_pos) 
    snake_stamp = snake.stamp()   
    stamp_list.append(snake_stamp)


#the main loop

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for pieces  in range(START_LENGTH):
    x_pos=snake.xcor() #Get x-position with snake.pos()[0]
    y_pos=snake.ycor() 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE 

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position

def up():
    snake.forward(50)
def down():
    snake.back(50)
def left():
    snake.left(45)
def right():
    snake.right(45)

snake.onkeypress(up,'w')
snake.onkeypress(down,'s')
snake.onkeypress(left,'a')
snake.onkeypress(right,'d')
snake.listen()
   
turtle.mainloop()




