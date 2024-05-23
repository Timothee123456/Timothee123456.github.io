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
left()
pat.forward(50)
left()
pat.pendown()



# draw the knife
pat.fillcolor("grey")
pat.begin_fill()
pat.forward(300)
pat.left(150)
pat.forward(150)
pat.left(30)
pat.forward(170)
left()
pat.forward(75)
pat.end_fill()

# draw the handle
pat.fillcolor("maroon")
pat.begin_fill()
right()
pat.forward(175)
right()
pat.forward(50)
right()
pat.forward(175)
pat.end_fill()


