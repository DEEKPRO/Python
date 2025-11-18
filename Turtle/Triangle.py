# Importing turtle
import turtle
from turtle import *

# Turtle Stary Triangle
fillcolor('lawngreen')
pencolor('crimson')
width(10)

a = 120
b = 300
begin_fill()
forward(b)
left(a)
forward(b)
left(a)
forward(b)
left(a)
end_fill()
penup()
right(180)
forward(100)
pendown()
pencolor('black')
fillcolor('orange')
begin_fill()
forward(b)
left(-a)
forward(b)
left(-a)
forward(b)
left(-a)
end_fill()
