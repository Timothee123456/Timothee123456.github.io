import turtle
import random
pat = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colours = ["cyan", "purple", "white", "blue", "red", "yellow", "magenta"]

pat.width(5)
pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            pat.color(random.choice(colours))
            pat.forward(30)
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
    pat.right(90)


for i in range(7):
    branch()
    pat.forward(90)
    pat.left(45)
branch()
