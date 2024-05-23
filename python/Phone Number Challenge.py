# instructions
print("Find the phone number with the illustration. Do not write a space between the numbers.")


# import turtle
import turtle
pat = turtle.Turtle()
turtle.Screen().bgcolor("pink")
pat.penup()
pat.home()
pat.left(90)
pat.forward(150)
pat.left(90)
pat.forward(100)
pat.right(180)

def star():
    pat.pendown()
    pat.right(15)
    pat.color("black")
    pat.fillcolor('white')
    pat.begin_fill()
    for i in range(5):
        pat.forward(10)
        pat.left(108)
        pat.forward(10)
        pat.right(36)
    pat.end_fill()
    pat.left(15)
    pat.penup()


# draw the stars
for i in range(3):
    for i in range (3):
        star()
        pat.forward(100)
    pat.backward(300)
    pat.right(90)
    pat.forward(100)
    pat.left(90)
pat.forward(100)
star()

# going back to start point
pat.width(5)
pat.left(90)
pat.forward(300)
pat.left(90)
pat.forward(100)
pat.left(90)
pat.backward(10)


# drawing the lines
pat.pendown()
pat.forward(100)
pat.left(135)
pat.forward(141.42)
pat.right(135)
pat.forward(100)
pat.right(45)
pat.forward(141.42)
pat.left(135)
pat.forward(100)
pat.right(90)
pat.forward(100)
pat.left(135)
pat.forward(141.42)
pat.left(45)
pat.forward(100)
pat.forward(100)
               
# answer
answer = input("What is the phone number? ")
while answer != "1425780963":
    print("Wrong number - try again!")
    answer = input("What is the phone number? ")
print("YOU WIN!!!")

