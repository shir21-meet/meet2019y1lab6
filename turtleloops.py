import turtle
turtle.left(110)
turtle.bgcolor('black')
turtle.color('red')
turtle.pensize(20)
num_pts=5
for i in range(num_pts):
    turtle.left(720/num_pts)
    turtle.forward(200)
    print (i)
turtle.mainloop()
