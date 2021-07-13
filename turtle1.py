import turtle 
t =turtle.Turtle()
screen = turtle.speed(0)
t.pen (pencolor = "blue")
t.shapesize (1,1,1)
t.pensize (10)
turtle.bgcolor ("yellow")
i =300
while True :
    t.circle (i)
    i -= i/2
    i =i/6


turtle.mainloop()
