import turtle

times = 10

def Line(x):
    for i in range(x):
        turtle.speed(100000)
        turtle.forward(10)
        turtle.lt(90)
        turtle.forward(2)
        turtle.rt(180)
        turtle.forward(2)
        turtle.lt(90)

def Graph():
    turtle.goto(0,0)
    for i in range(4):
        Line(30)
        turtle.goto(0,0)
        turtle.rt(90)
    
def yintercept(y):
    yintercept = y * 10
    turtle.goto(0, yintercept)
    coords = (turtle.xcor(), turtle.ycor())
    print(coords)

def Draw(rise , run):
    for i in range(times):
        Rise = rise * 10
        Run = run * 10
        turtle.goto(turtle.xcor() + Run, turtle.ycor() + Rise)

def Reset():
    for i in range(times):
        turtle.undo()
