from turtle import *

speed(50)
width(3)

for i in range(4):
    forward(200)
    left(90)

penup()
goto(0, 300)
pendown()

for i in range(4):
    forward(200)
    left(90)

penup()
goto(-300, 0)
pendown()

for i in range(4):
    forward(200)
    left(90)

penup()
goto(-300,300)
pendown()

for i in range(4):
    forward(200)
    left(90)

exitonclick()