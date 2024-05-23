import turtle
pat = turtle.Turtle()
turtle.Screen().bgcolor("white")


def right(): {
    pat.right(90)
    }

def left(): {
    pat.left(90)
    }

# reset
pat.width(5)
pat.penup()
pat.forward(200)
right()
pat.forward(200)
left()
left()
pat.pendown()



# draw the book
pat.fillcolor("deepskyblue")
pat.begin_fill()
pat.forward(500)
left()
pat.forward(400)
left()
pat.forward(500)
left()
pat.forward(400)
pat.end_fill()


# draw the grass
pat.fillcolor("lawngreen")
pat.begin_fill()
left()
pat.forward(100)
left()
pat.forward(400)
left()
pat.forward(100)
left()
pat.forward(400)
pat.end_fill()


# go to location
pat.penup()
left()
pat.forward(100)
left()
pat.forward(75)
right()
pat.pendown()


# draw the house
pat.fillcolor("red")
pat.begin_fill()
pat.forward(200)
left()
pat.forward(250)
left()
pat.forward(200)
left()
pat.forward(250)
pat.end_fill()


# go to location
pat.penup()
left()
pat.forward(200)
pat.left(45)
pat.pendown()


# draw the roof
pat.fillcolor("darkorchid")
pat.begin_fill()
pat.forward(177)
left()
pat.forward(177)
pat.left(135)
pat.forward(250)
pat.end_fill()


# go to location
pat.penup()
right()
pat.forward(200)
right()
pat.forward(100)
right()
pat.pendown()


# draw the door
pat.fillcolor("maroon")
pat.begin_fill()
pat.forward(90)
left()
pat.forward(50)
left()
pat.forward(90)
left()
pat.forward(50)
pat.end_fill()


# go to location
pat.penup()
left()
pat.forward(55)
left()
pat.forward(10)
pat.pendown()


# draw the door nob
pat.width(2)
pat.fillcolor("yellow")
pat.begin_fill()
pat.circle(5)
pat.end_fill()



def drawWindow(color):
    # draw the window
    pat.width(4)
    pat.fillcolor(color)
    pat.begin_fill()
    for i in range (4):
        pat.forward(50)
        left()
    pat.end_fill()
    pat.forward(25)
    left()
    pat.forward(50)
    for i in range (2):
        right()
        pat.forward(25)
    right()
    pat.forward(50)


# go to location
pat.penup()
right()
pat.forward(90)
left()
pat.forward(70)
pat.pendown()

drawWindow("yellow")

# go to location
pat.penup()
right()
pat.forward(25)
left()
pat.forward(110)
pat.pendown()

drawWindow("yellow")

# go to location
pat.penup()
right()
pat.forward(100)
left()
pat.forward(60)
pat.right(135)
pat.forward(58)
left()
pat.pendown()

drawWindow("#5c4a4a")

pat.hideturtle()