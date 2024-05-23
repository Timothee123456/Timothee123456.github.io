import turtle
pat = turtle.Turtle()
turtle.Screen().bgcolor("white")

pat.width(5)
pat.fillcolor("olive")
pat.penup()
pat.backward(100)
pat.pendown()





def right(): {
    pat.right(90)
    }

def left(): {
    pat.left(90)
    }

def notch (up, forward1, forward2): {
    right(),
    pat.forward(up),
    left(),
    pat.forward(forward1),
    left(),
    pat.forward(up),
    right(),
    pat.forward(forward2)
}



# draw the key
pat.begin_fill()
pat.forward(300)
left()
pat.forward(30)
left()
pat.forward(30)
notch (30, 50, 10)
notch (10, 20, 20)
notch (15, 45, 10)
notch (25, 10, 10)
pat.forward(95)
right()
pat.forward(20)
left()
pat.forward(100)
left()
pat.forward(70)
left()
pat.forward(100)
left()
pat.forward(20)
pat.end_fill()


