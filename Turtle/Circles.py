import turtle
from turtle import *
pencolor('yellow')
width(2)
speed(0)
bgcolor('black')
penup()
left(90)
forward(40)
right(90)
pendown()
fillcolor('orangered')
def circle():
    begin_fill()
    for i in range(72):
        for i in range(72):
            forward(2)
            left(5)
        forward(10)
        right(5)
    end_fill()
    return
print(circle())
