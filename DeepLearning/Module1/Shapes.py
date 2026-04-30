import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("orangered")
screen = turtle.Screen()
screen.setup(800, 800, 100, 100)
t.speed(3)

for _ in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(-150, -100)
t.pendown()

for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80) 
    t.left(90)

t.penup()
t.goto(100, -200)
t.pendown()

for _ in range(6):
    t.forward(70)
    t.left(60)
