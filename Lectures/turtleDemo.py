import turtle, threading
from random import *

num = randint(1, 2)

def DrawRectangle(tur, x = 0, y = 0, width=100, height = 100):

    tur.penup()
    tur.goto(x, y)
    tur.pendown()

    for i in range(2):
        tur.forward(width)
        tur.left(90)
        tur.forward(height)
        tur.left(90)

def changeColour(idx):
    idx = idx % 4
    
    if idx == 0:
        return "red"

    elif idx == 1:
        return "blue"

    elif idx == 2:
        return "green"

    else:
        return "black"

def main():
    n = eval(input("Enter an integer: "))
    
    tur = turtle.Turtle()
    tur.pensize(5)

    for i in range(n):

        tur.color(changeColour(i))
        gap = 200 * i - 300
        DrawRectangle(tur, x= gap)

main()

''' 숙제
def DrawRectangle(tur, width = 10, height = 10, bottomLeftX = 0, bottomLeftY = 0):
    tur.penup()
    tur.goto(bottomLeftX, bottomLeftY)
    tur.pendown()
    for i in range(2):
        tur.forward(width)
        tur.left(90)
        tur.forward(height)
        tur.left(90)


def DrawTriangle(tur, sideLength = 10, bottomLeftX = 0, bottomLeftY = 0):
    tur.penup()
    tur.goto(bottomLeftX, bottomLeftY)
    tur.pendown()
    for i in range(3):
        tur.forward(sideLength)
        tur.left(120)


##create turtle objects
a = turtle.Turtle()

a.pensize(5)


## draw a rect
#DrawRectangle(a, 123, 145)
#DrawRectangle(a)

#region 숙제
# initial point (-300, 0)
a.pencolor("green")
DrawTriangle(a, 300, -200)
a.pencolor("black")
DrawRectangle(a, 300, -300, -200)

a.pencolor("blue")
DrawRectangle(a, 100, 100, -180, -120)
DrawRectangle(a, 100, 100, -20, -120)

a.pencolor("red")
DrawRectangle(a, 100, 150, -100, -300)
#endregion

#DrawTriangle(a, 100, 100, -50)


#a.pencolor("red")
#a.circle(100, 360)
'''

input("Press Enter to Exit")


