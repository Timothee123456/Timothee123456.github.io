import turtle
pat = turtle.Turtle()
turtle.Screen().bgcolor("grey")
pat.fillcolor("white")
pat.width(5)

def right(): {
    pat.right(90)
    }

def left(): {
    pat.left(90)
    }

def door():
    pat.penup()
    pat.forward(25)
    pat.pendown()
    

# go to location
pat.penup()
pat.backward(35)
left()
pat.backward(100)
pat.pendown()



# draw the hall
pat.begin_fill()
pat.forward(250)
right()
pat.forward(50)
door()
pat.forward(50)
right()
pat.forward(112.5)
door()
pat.forward(112.5)
right()
pat.forward(50)
door()
pat.forward(50)
pat.end_fill()


# go to location
pat.penup()
right()
pat.forward(250)
right()
pat.backward(50)
pat.pendown()

# draw the bedroom
pat.begin_fill()
pat.forward(100)
door()
pat.forward(125)
left()
pat.forward(150)
left()
pat.forward(250)
left()
pat.forward(62.5)
door()
pat.forward(62.5)
pat.end_fill()


# go to location
pat.penup()
pat.backward(100)
pat.pendown()

# draw the bathroom
pat.begin_fill()
pat.forward(12.5)
door()
pat.forward(12.5)
right()
pat.forward(100)
right()
pat.forward(50)
right()
pat.forward(100)
pat.end_fill()


# go to location
pat.penup()
pat.forward(175)
right()
pat.forward(150)
pat.pendown()

# draw the dining room
pat.begin_fill()
pat.forward(62.5)
door()
pat.forward(62.5)
left()
pat.forward(200)
left()
pat.forward(150)
left()
pat.forward(200)
pat.end_fill()



# go to location
pat.penup()
left()
pat.forward(200)
right()
pat.backward(12.5)
pat.pendown()

# draw the kitchen
pat.begin_fill()
pat.forward(62.5)
door()
pat.forward(62.5)
left()
pat.forward(62.5)
door()
pat.forward(62.5)
left()
pat.forward(150)
left()
pat.forward(150)
pat.end_fill()


# go to location
pat.penup()
left()
pat.forward(150)
right()
pat.forward(50)
left()
pat.pendown()

# draw the living room
pat.begin_fill()
pat.forward(75)
pat.width(10)
pat.forward(50)
pat.width(5)
pat.forward(75)
left()
pat.forward(250)
left()
pat.forward(200)
left()
pat.forward(112.5)
door()
pat.forward(112.5)
pat.end_fill()