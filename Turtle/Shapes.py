import turtle
from turtle import *
shape = int(input('How many sides should there be on this shape? : '))
def stage(bg, fill, pen):
    bgcolor(bg)
    fillcolor(fill)
    pencolor(pen)
    width(3)
    penup()
    left(90)
    forward(250)
    right(90)
    pendown()
print(stage('black', 'orangered', 'green'))
def circle(fow, rig):
    begin_fill()
    fow = int(fow)
    rig = int(rig)
    for i in range(shape):
        forward(fow)
        right(rig)
    end_fill()
f = int(input('How large should the circle be? :'))
c = int(input('How curvy should the circle be? :'))
print(circle(f, c))

    
