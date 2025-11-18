#Importing turtle
import turtle
from turtle import *
bgcolor('black')
fillcolor('cyan')
f = 200
pensize(5)
pencolor('white')
penup()
backward(f)
right(90)
pendown()
#Creating a square
begin_fill()
for i in range(4):
    forward(f)
    left(90)
end_fill()
#Now the triangle
fillcolor('brown')
begin_fill()
left(135)
forward(143)
right(90)
forward(143)
end_fill()
#Time for the windows
right(45)
forward(50)
right(90)
penup()
forward(30)
pendown()
for i in range(4):
    forward(50)
    left(90)
penup()
forward(f/2)
pendown()
for i in range(4):
    forward(50)
    left(90)
