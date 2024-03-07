from turtle import *


#we wont to paint a house

#step 1:draw a aquare
speed(30)
width(7)
color ("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)  
color("yellow")
begin_fill()
left(90)
forward(120)      #heightof the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of door

#drawing a window
begin_fill()
color("blue")
goto(0, 120)
left(120)
forward(50)
left(90)
forward(80)
end_fill()

begin_fill()
right(90)
forward(150)
right(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
end_fill()


exitonclick()