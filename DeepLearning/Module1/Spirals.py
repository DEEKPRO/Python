import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("black")
screen = turtle.Screen()
screen.setup(800, 800, 100, 100)
t.speed("fastest")
t.hideturtle()
li = ["red", "green", "blue", "orange", "yellow", "purple"]
while True:
    for x in range(0, 199):
        t.pencolor(li[x%len(li)])
        t.width(x/100+1)
        t.forward(x)
        t.left(59)
    t.right(239)
    for x in range(200, 0, -1):
        t.pencolor("red")
        t.width(x/100+7)
        t.forward(x)
        t.right(59)