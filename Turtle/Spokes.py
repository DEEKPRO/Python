#Importing turtle for drawing
import turtle
from turtle import *
#Drawing the spokes
y = input('Enter a color: ')
pencolor(y)
pensize('5')
d = int(input('How many spikes? : '))
x = 360/d
for i in range(d):
    forward(100)
    backward(100)
    left(x)
print('Thank You!!!')
