#!/bin/python3

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    ORANGE = '\033[33m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Turtle
import turtle
import random
import time

# Snowflake
def snowflake():
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


# Torch
def torch():
    pat = turtle.Turtle()
    turtle.Screen().bgcolor("white")


    def right(): {
        pat.right(90)
        }

    def left(): {
        pat.left(90)
        }

    def rectangle(side1, side2):
        pat.begin_fill()
        for i in range (2):
            pat.forward(side1)
            right()
            pat.forward(side2)
            right()
        pat.end_fill()

    # reset
    pat.width(5)
    pat.penup()
    left()
    pat.forward(50)
    right()
    pat.backward(200)
    pat.pendown()



    # draw the handle
    pat.fillcolor("grey")
    rectangle(20, 75)
    pat.forward(20)
    rectangle(300, 75)
    pat.forward(300)

    # draw the light
    pat.fillcolor("yellow")
    pat.begin_fill()
    pat.left(45)
    pat.forward(100)
    pat.right(135)
    pat.forward(215)
    pat.right(135)
    pat.forward(100)
    pat.right(45)
    pat.forward(75)
    pat.end_fill()

    # go to location
    pat.penup()
    pat.backward(30)
    right()
    pat.backward(125)
    pat.pendown()

    # draw switch
    pat.fillcolor("darkgrey")
    rectangle(25, 15)
    pat.forward(25)
    rectangle(25, 15)



# Knife
def knife():
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
    right()
    pat.forward(50)
    pat.end_fill()

# Key
def key():
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

    # write date
    pat.penup()
    right()
    pat.forward(300)
    left()
    pat.forward(40)
    right()
    pat.backward(65)
    pat.write(1986)
# Book
def book():
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

# Map
def Map():
    pat = turtle.Turtle()
    turtle.Screen().bgcolor("grey")
    pat.fillcolor("white")
    pat.width(5)

    # stairs
    size = 2
    def stairs():
        pat.width(size)
        pat.right(180)
        for i in range(5):
            right()
            pat.forward(4 * size)
            left()
            pat.forward(4 * size)
        for i in range (2):
            left()
            pat.forward(20 * size)
        # line
        pat.penup()
        left()
        pat.forward(8 * size)
        pat.left(45)
        pat.backward(5 * size)
        pat.pendown()

    def stairsUp():
        stairs()
        pat.forward(28 * size)
        left()
        for i in range (2):
            pat.left(60)
            pat.forward(4 * size)
            pat.backward(4 * size)
            
    def stairsDown():
        stairs()
        pat.penup()
        pat.forward(28 * size)
        pat.pendown()
        pat.right(180)
        pat.forward(28 * size)
        left()
        for i in range (2):
            pat.left(60)
            pat.forward(4 * size)
            pat.backward(4 * size)
        pat.right(165)

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
    pat.forward(75)
    door()
    pat.forward(100)
    left()
    pat.forward(150)
    left()
    pat.forward(200)
    pat.end_fill()



    # go to location
    left()
    pat.penup()
    pat.forward(150)
    left()
    pat.forward(12.5)
    right()
    pat.pendown()

    # draw the library
    pat.begin_fill()
    pat.forward(112.5)
    door()
    pat.forward(100)
    left()
    pat.forward(150)
    left()
    pat.forward(237.5)
    left()
    pat.forward(62.5)
    door()
    pat.forward(62.5)
    pat.end_fill()



    # go to location
    pat.penup()
    left()
    pat.forward(50)
    right()
    pat.pendown()

    # draw the kitchen
    for i in range (2):
        pat.begin_fill()
        pat.forward(62.5)
        door()
        pat.forward(62.5)
        left()
    pat.forward(150)
    left()
    pat.forward(62.5)
    door()
    pat.forward(62.5)
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
    pat.forward(112.5)
    door()
    pat.forward(112.5)
    left()
    pat.forward(200)
    left()
    pat.forward(112.5)
    door()
    pat.forward(112.5)
    pat.end_fill()


    # go to location
    pat.penup()
    pat.backward(145)
    right()
    pat.backward(220)
    pat.pendown()

    # draw the stairs
    stairsUp()

    pat.hideturtle()

# Map2
def Map2():
    pat = turtle.Turtle()
    turtle.Screen().bgcolor("grey")
    pat.fillcolor("white")
    pat.width(5)

    def right():
        pat.right(90)

    def left():
        pat.left(90)
        
        
    # stairs
    size = 2
    def stairs():
        pat.width(size)
        pat.right(180)
        for i in range(5):
            right()
            pat.forward(4 * size)
            left()
            pat.forward(4 * size)
        for i in range (2):
            left()
            pat.forward(20 * size)
        # line
        pat.penup()
        left()
        pat.forward(8 * size)
        pat.left(45)
        pat.backward(5 * size)
        pat.pendown()

    def stairsUp():
        stairs()
        pat.forward(28 * size)
        left()
        for i in range (2):
            pat.left(60)
            pat.forward(4 * size)
            pat.backward(4 * size)
            
    def stairsDown():
        stairs()
        pat.penup()
        pat.forward(28 * size)
        pat.pendown()
        pat.right(180)
        pat.forward(28 * size)
        left()
        for i in range (2):
            pat.left(60)
            pat.forward(4 * size)
            pat.backward(4 * size)
        pat.right(165)

        

    def door():
        pat.penup()
        pat.forward(25)
        pat.pendown()
        
    def door2():
        pat.forward(82.5)
        door()
        pat.forward(82.5)
        right()
        
    def wall():
        pat.forward(190)
        right()
        
    def location():
        pat.penup()
        pat.forward(190)
        pat.pendown()
        
        
        
    # go to location
    pat.penup()
    right()
    pat.forward(50)
    left()
    pat.backward(390)
    pat.pendown()

    # draw the stairs and reset
    stairsDown()
    pat.width(5)
    pat.penup()
    pat.forward(20)
    left()
    pat.forward(100)
    right()
    pat.pendown()


    # draw the red bedroom
    pat.begin_fill()
    for i in range (2):
        door2()
    wall()
    door2()
    pat.end_fill()

    # draw the green bedroom
    location()
    pat.begin_fill()
    wall()
    for i in range (3):
        door2()
    pat.end_fill()
        
    # draw the blue bedroom
    location()
    pat.begin_fill()
    for i in range (2):
        door2()
    wall()
    door2()
    pat.end_fill()

    # draw the yellow bedroom
    location()
    pat.begin_fill()
    for i in range (2):
        wall()
    for i in range (2):
        door2()
    pat.end_fill()

    # go to location
    pat.penup()
    pat.backward(525)
    pat.pendown()
    left()

    # draw the bathroom
    pat.begin_fill()
    pat.forward(150)
    right()
    pat.forward(100)
    right()
    pat.forward(150)
    right()
    pat.forward(37.5)
    door()
    pat.forward(37.5)
    pat.end_fill()

    # go to location
    pat.penup()
    pat.backward(335)
    right()
    pat.pendown()

    # draw the study
    pat.begin_fill()
    for i in range (3):
        wall()
    door2()
    pat.end_fill()

    # go to location
    pat.penup()
    pat.backward(190)
    left()
    pat.forward(150)
    left()
    pat.pendown()

    # draw the closet
    pat.begin_fill()
    pat.forward(30)
    left()
    pat.forward(110)
    left()
    pat.forward(30)
    left()
    pat.forward(42.5)
    door()
    pat.forward(42.5)
    pat.end_fill()

    # go to location
    pat.penup()
    pat.backward(340)
    left()
    pat.pendown()

    # draw the closet
    pat.begin_fill()
    pat.forward(40)
    left()
    pat.forward(190)
    left()
    pat.forward(40)
    left()
    pat.forward(82.5)
    door()
    pat.forward(82.5)
    pat.end_fill()

    pat.hideturtle()




# Recipe
def recipe():
    print(color.GREEN + "Vanilla Cake")
    time.sleep(0.5)
    print("=============================================================================================================================================================================================================")
    time.sleep(0.5)
    print("")
    time.sleep(0.5)
    print("Ingredients:")
    time.sleep(0.5)
    print("- 2 cups (250g) all-purpose flour")
    time.sleep(0.5)
    print("- 2 teaspoons baking powder")
    time.sleep(0.5)
    print("- 1/2 teaspoon salt")
    time.sleep(0.5)
    print("- 1/2 cup (115g) unsalted butter, at room temperature")
    time.sleep(0.5)
    print("- 1 1/4 cups (250g) granulated sugar")
    time.sleep(0.5)
    print("- 3 large eggs, at room temperature")
    time.sleep(0.5)
    print("- 1 tablespoon vanilla extract")
    time.sleep(0.5)
    print("- 1 cup (240ml) milk, at room temperature")
    time.sleep(0.5)
    print("")
    time.sleep(0.5)
    print("Frosting:")
    time.sleep(0.5)
    print("- 1 cup (230g) unsalted butter, at room temperature")
    time.sleep(0.5)
    print("- 4 cups (480g) confectioners' sugar")
    time.sleep(0.5)
    print("- 2 tablespoons heavy cream (or milk)")
    time.sleep(0.5)
    print("- 1 teaspoon vanilla extract")
    time.sleep(0.5)
    print("- 1/4 teaspoon salt")
    time.sleep(0.5)
    print("")
    time.sleep(0.5)
    print("Instructions:")
    time.sleep(0.5)
    print("1. Preheat the oven to 350°F (177°C). Grease and flour two 9-inch round cake pans.")
    time.sleep(0.5)
    print("2. In a medium bowl, whisk together the flour, baking powder, and salt. Set aside.")
    time.sleep(0.5)
    print("3. In a large bowl, beat the butter and sugar together until light and fluffy, about 2-3 minutes. Beat in the eggs one at a time, then stir in the vanilla.")
    time.sleep(0.5)
    print("4. Gradually add the dry ingredients to the wet ingredients, alternating with the milk, mixing just until incorporated. Avoid overmixing.")
    time.sleep(0.5)
    print("5. Divide the batter evenly between the prepared cake pans.")
    time.sleep(0.5)
    print("6. Bake for 30-35 minutes, or until a toothpick inserted in the center comes out clean.")
    time.sleep(0.5)
    print("7. Allow the cakes to cool in the pans for 10 minutes, then transfer to a wire rack to cool completely.")
    time.sleep(0.5)
    print("8. For the frosting, beat the butter in a large bowl until creamy. Gradually add the confectioners' sugar and beat until smooth. Add the heavy cream, vanilla, and salt, and beat until light and fluffy.")
    time.sleep(0.5)
    print("9. Spread the frosting between the two cake layers and on the top and sides of the cake.")
    time.sleep(0.5)
    print("10. Refrigerate the cake for at least 2 hours before serving to allow the frosting to set.")
    time.sleep(0.5)
    print("=============================================================================================================================================================================================================" +color.END)
    time.sleep(1)


# Phone Number Challenge
def phoneNumberChallenge():
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


def password():
    import turtle
    pat = turtle.Turtle()
    turtle.Screen().bgcolor("deepskyblue")

    blockSize = 40

    def right(): {
        pat.right(90)
        }

    def left(): {
        pat.left(90)
        }

    # reset
    pat.speed(10)
    pat.penup()
    pat.backward(blockSize * 7.5)
    left()
    pat.forward(blockSize * 7.5)
    right()
    pat.pendown()


    # draw the framing
    def framing():
        pat.begin_fill()
        for i in range (5):
            pat.forward(blockSize * 15)
            pat.backward(blockSize * 15)
            right()
            pat.forward(blockSize)
            left()
        pat.forward(blockSize)
        left()
        for i in range (14):
            pat.forward(blockSize * 5)
            pat.backward(blockSize * 5)
            right()
            pat.forward(blockSize)
            left()
        pat.forward(blockSize * 5)
        pat.end_fill()
        
        
    def square():
        pat.pendown()
        pat.begin_fill()
        for i in range (4):
            pat.forward(blockSize)
            right()
        pat.end_fill()
        pat.penup()

    def square2():
        left()
        square()
        right()


    def line():
        for i in range (2):
            square()
            right()
            pat.forward(blockSize * 2)
            left()
        square()
        left()
        pat.forward(blockSize * 4)
        right()
        pat.forward(blockSize * 2)
        
    def cross2():
        right()
        pat.forward(blockSize * 1)
        left()

    def cross():
        cross2()
        square()
        pat.forward(blockSize * 2)
        square()
        pat.backward(blockSize * 2)
        cross2()
        pat.forward(blockSize * 1)
        square()
        pat.backward(blockSize * 1)
        cross2()
        square()
        pat.forward(blockSize * 2)
        square()
        pat.forward(blockSize * 1)
        left()
        pat.forward(blockSize * 3)
        right()
        
        
    # frames
    pat.fillcolor("white")    
    framing()
    pat.penup()
    pat.backward(blockSize * 10)
    right()
    pat.backward(blockSize * 15)
    pat.pendown()
    framing()

    # going to location
    pat.penup()
    pat.forward(blockSize * 10)
    right()
    pat.backward(blockSize * 15)

    # colouring top
    pat.fillcolor("red")
    line()
    square()
    right()
    pat.forward(blockSize * 4)
    left()
    square()
    left()
    pat.forward(blockSize * 4)
    right()
    pat.forward(blockSize * 2)
    for i in range (4):
        line()
    pat.forward(blockSize)
    line()

    # going to location
    right()
    pat.forward(blockSize * 10)
    left()
    pat.backward(blockSize * 15)

    # colouring bottom
    pat.fillcolor("green")
    right()
    pat.forward(blockSize)
    square2()
    pat.forward(blockSize * 2)
    square2()
    pat.backward(blockSize * 3)
    left()
    pat.forward(blockSize)
    right()
    square2()
    pat.forward(blockSize * 4)
    square2()
    pat.backward(blockSize * 4)
    left()
    pat.forward(blockSize * 2)
    cross()
    pat.forward(blockSize * 2)
    square()
    pat.backward(blockSize)
    cross()
    # T
    pat.forward(blockSize)
    square()
    pat.forward(blockSize * 2)
    square()
    pat.backward(blockSize)
    right()
    pat.forward(blockSize)
    square2()
    pat.forward(blockSize * 2)
    square2()
    pat.hideturtle()

def paper4():
    import turtle
    pat = turtle.Turtle()
    turtle.Screen().bgcolor("grey")

    pat.color("white")


    # reset
    pat.width(10)
    pat.penup()
    pat.forward(50)
    pat.right(90)
    pat.forward(300)
    pat.left(90)
    pat.backward(150)
    pat.pendown()

    # draw 1
    pat.forward(300)
    pat.backward(150)
    pat.left(90)
    pat.forward(600)
    pat.left(135)
    pat.forward(200)

def paper3():
    import turtle
    pat = turtle.Turtle()
    turtle.Screen().bgcolor("grey")

    pat.color("white")


    # reset
    pat.width(10)
    pat.penup()
    pat.left(90)
    pat.forward(300)
    pat.left(150)
    pat.pendown()

    # draw 4
    pat.forward(345)
    pat.left(120)
    pat.forward(275)

    pat.penup()
    pat.backward(100)
    pat.left(90)
    pat.backward(150)
    pat.pendown()
    
    pat.forward(450)

def paper2():
    import turtle
    pat = turtle.Turtle()
    turtle.Screen().bgcolor("grey")

    pat.color("white")


    # reset
    pat.width(10)
    pat.penup()
    pat.backward(200)
    pat.left(90)
    pat.forward(300)
    pat.right(90)
    pat.pendown()

    # draw 7
    pat.forward(400)
    pat.right(120)
    pat.forward(670)

def paper1():
    import turtle
    pat = turtle.Turtle()
    turtle.Screen().bgcolor("grey")

    pat.color("white")


    # reset
    pat.width(10)
    pat.penup()
    pat.forward(150)
    pat.left(90)
    pat.forward(150)
    pat.pendown()

    # draw 8
    pat.circle(150)
    pat.penup()
    pat.backward(300)
    pat.pendown()
    pat.circle(150)

# Open safe function
def openSafeKey():
    print("The password contains 4 numbers")
    print('Type "exit" to exit')
    answer = input("What is the password? ")
    while answer != "1478" and answer != "exit":
        print("Wrong password - try again!")
        answer = input("What is the password? ")
    if answer != "exit":
        # display a helpful message
        print("You opened the safe and found a " + rooms[currentRoom]['safe'] +"!")
        # add the item to their inventory
        inventory.append("bucket")
        # delete the safe from the room
        del rooms[currentRoom]['safe']


def openSafeRecipe():
    # clear screen
    turtle.resetscreen()
    print("There is an image on the safe, here it is...")
    time.sleep(2)
    phoneNumberChallenge()
    print("The password is a phone number (do not include the spaces)")
    print('Type "exit" to exit')
    answer = input("What is the phone number? ")
    while answer != "1425780963" and answer != "exit":
        print("Wrong number - try again!")
        answer = input("What is the phone number? ")
    if answer != "exit":
        # display a helpful message
        print("You opened the safe and found a " + rooms[currentRoom]['safe'] +"!")
        # add the item to their inventory
        inventory.append("bucket")
        # delete the safe from the room
        del rooms[currentRoom]['safe']
        
        
def openSafeTorch():
    # clear screen
    turtle.resetscreen()
    print("There is an image on the safe, here it is...")
    time.sleep(2)
    password()
    print("The password contains 4 letters (all in capitals)")
    print('Type "exit" to exit')
    answer = input("What is the password? ")
    while answer != "CHAT" and answer != "exit":
        print("Wrong password - try again!")
        answer = input("What is the password? ")
    if answer != "exit":
        # display a helpful message
        print("You opened the safe and found a " + rooms[currentRoom]['safe'] +"!")
        # add the item to their inventory
        inventory.append("bucket")
        # delete the safe from the room
        del rooms[currentRoom]['safe']
        
        
def openSafeBucket():
    print("The password contains 5 numbers")
    print('Type "exit" to exit')
    answer = input("What is the password? ")
    while answer != "51951" and answer != "exit":
        print("Wrong password - try again!")
        answer = input("What is the password? ")
    if answer != "exit":
        # display a helpful message
        print("You opened the safe and found a " + rooms[currentRoom]['safe'] +"!")
        # add the item to their inventory
        inventory.append("bucket")
        # delete the safe from the room
        del rooms[currentRoom]['safe']

def paper():
    print('A number is on the piece of paper, here it is: ' + color.BOLD + '51951' + color.END)


def open4():
    print("Here is the story:")
    time.sleep(2)
    print('A priceless medival chess was stolen at the Games Museum.')
    time.sleep(4)
    print('It was during the opening hours.')
    time.sleep(2)
    print('The chess board was enclosed in a dispay case. It took skill to open it.')
    time.sleep(5)
    print("The room's security was unplugged at midday.")
    time.sleep(2.5)
    print('But the camera in the corridor shows who came in and when.')
    time.sleep(4)
    print('')
    print('Here is the list of suspects:')
    time.sleep(2)
    print('Dice Shaker, German. Games collector.')
    time.sleep(0.5)
    print('Entered at 2:08pm. Exited at 2:43pm.')
    time.sleep(0.5)
    print('Dressed with a large coat.')
    time.sleep(8)
    print('')
    print('Lizzie Board, English Scrabble champion.')
    time.sleep(0.5)
    print('Entered at 2:12pm. Exited at 3:36pm.')
    time.sleep(0.5)
    print('Dressed with a large jaket.')
    time.sleep(8)
    print('')
    print('Erica Valiere, Italian Chess champion.')
    time.sleep(0.5)
    print('Entered at 3:23pm. Exited at 4;20pm.')
    time.sleep(0.5)
    print('Dressed in shorts and t-shirt.')
    time.sleep(8)
    print('')
    print('Fabien Roulette, French. Specialist antique dealer.')
    time.sleep(0.5)
    print('Entered at 4:15pm. Exited at 4:42pm.')
    time.sleep(0.5)
    print('Dressed with a large coat.')
    time.sleep(8)
    print('')
    print('The chessboard can be folded to store the pieces inside...')
    time.sleep(4)
    print("It's still bulky, but it could be hidden under baggy clothes.")
    time.sleep(4)
    print('The thief left a message with the Scrabble. Here it is:')
    time.sleep(3.5)
    print('          C')
    time.sleep(0.5)
    print('          H')
    time.sleep(0.5)
    print('    M A T E')
    time.sleep(0.5)
    print('          Q')
    time.sleep(0.5)
    print('          U')
    time.sleep(0.5)
    print('          E')
    time.sleep(1)
    print('There are no fingerprints, the thief took care to put on gloves or wipe everything...')
    time.sleep(5)
    print('It was a pro thief but not a pro player! One wrong move clears one suspect.')
    time.sleep(5)
    print('')
    print("Who was the thief? ")
    time.sleep(1)
    print("Dice Shaker")
    time.sleep(0.5)
    print("Lizzie Board")
    time.sleep(0.5)
    print("Erica Valiere")
    time.sleep(0.5)
    print("Fabien Roulette")
    time.sleep(0.5)
    print("Type 'exit' to exit")
    answer = input(">")
    while answer != "Fabien Roulette" and answer != "exit":
        print(color.BOLD + "Wrong person!!!")
        time.sleep(0.5) 
        print(color.RED + "YOU LOOSE!!!😧😧😧")
        # loop forever
        while True:
           time.sleep(0.5) 
    if answer != "exit":
        # display a helpful message
        print("You opened the safe and found a piece of paper...")
        # add the item to their inventory
        inventory.append("bucket")
        # delete the safe from the room
        del rooms[currentRoom]['safe']
        

def open2():
    print("Here is the story:")
    time.sleep(2)
    print('You are on a boat.')
    time.sleep(2)
    print('The fuel tank is empty.')
    time.sleep(2)
    print('You found fuel drums.')
    time.sleep(2)
    print('But a note is on the wall. Here it is:')
    time.sleep(3)
    print('')
    print('  Four of these drums contain')
    time.sleep(0.5)
    print('enough fuel to get you safely to')
    time.sleep(0.5)
    print(' land. ' + color.BOLD + "It's easy. " + color.END + 'The 13 letters')
    time.sleep(0.5)
    print(' making up their names can be')
    time.sleep(0.5)
    print('   rearranged to spell mine.')
    time.sleep(0.5)
    print(color.BOLD + 'But beware! ' + color.END + 'The 9 other drums')
    time.sleep(0.5)
    print('will explode if they are opened.')
    time.sleep(0.5)
    print('                          Yours,')
    time.sleep(0.5)
    print('                Azul Izquierdad')
    time.sleep(10)
    print('')
    print('The code is the combination of the numbers of the fuel tanks:')
    time.sleep(3.5)
    print('Tank 1: DAC')
    time.sleep(1)
    print('Tank 2: RED')
    time.sleep(1)
    print('Tank 3: EDA')
    time.sleep(1)
    print('Tank 4: UQO')
    time.sleep(1)
    print('Tank 5: LUZ')
    time.sleep(1)
    print('Tank 6: ULIR')
    time.sleep(1)
    print('Tank 7: ARA')
    time.sleep(1)
    print('Tank 8: LEA')
    time.sleep(1)
    print('Tank 9: AIR')
    time.sleep(1)
    print('Tank 10: DIEZ')
    time.sleep(1)
    print('Tank 11: RAL')
    time.sleep(1)
    print('Tank 12: QUIZ')
    time.sleep(1)
    print('Tank 13: ZARD')
    time.sleep(3)
    print('There is one letter found in only one of the remaining drums.')
    time.sleep(3.2)
    print('From this, you can work out the lenght of the other three names...')
    time.sleep(3.2)
    print("Type 'exit' to exit")
    answer = input("What is the code? ")
    while answer != "35912" and answer != "exit":
        print(color.BOLD + "Wrong code!!!")
        time.sleep(0.5)
        print(color.RED + "YOU LOOSE!!! 😧😧😧")
        # loop forever
        while True:
           time.sleep(10) 
    if answer != "exit":
        # display a helpful message
        print("You opened the safe and found a piece of paper...")
        # add the item to their inventory
        inventory.append("bucket")
        # delete the safe from the room
        del rooms[currentRoom]['safe']



def open3():
    print("Here is the story:")
    time.sleep(2)
    print('You are envestigating a case.')
    time.sleep(2)
    print('Yesterday, a robot called V-Shnu was crushed under a 500L water tank.')
    time.sleep(4)
    print("It can't be an accident.")
    time.sleep(2)
    print("Here is V-Shnu's card:")
    time.sleep(2)
    print(color.PURPLE + "Strenght: can lift 230 kg")
    time.sleep(0.5)
    print("Power: solar")
    time.sleep(0.5)
    print("Speed: 80 km/h" + color.END)
    time.sleep(2)
    print("Only the other robots were present in the building when V-Shnu was destroyed, at 11:30 p.m.")
    time.sleep(5)
    print("But they have to respect these three robots laws:")
    time.sleep(3)
    print(color.ORANGE+ "A: A robot should never harm a human.")
    time.sleep(0.5)
    print("B: A robot should not harm another robot.")
    time.sleep(0.5)
    print("C: A robot should act to ensure its own survival." + color.END)
    time.sleep(8)
    print("Each robot applies the laws in a different order.")
    time.sleep(3)
    print("A robot who applies the laws in the order ACB will always respect Law A; Law C unless it goes against Law A; and Law B unless it goes against A or C.")
    time.sleep(11)
    print("Here are the suspects:")
    time.sleep(2)
    print('')
    print(color.BOLD + "K-Li" + color.END)
    time.sleep(0.5)
    print(color.PURPLE + "Strenght: 750 kilos")
    time.sleep(0.5)
    print("Power: hydrogen battery")
    time.sleep(0.5)
    print("It applies the laws in the order: ABC" + color.END)
    time.sleep(5)
    print('')
    print(color.BOLD + "Ga-Nesh" + color.END)
    time.sleep(0.5)
    print(color.PURPLE + "Strenght: 450 kilos")
    time.sleep(0.5)
    print("Power: solar")
    time.sleep(0.5)
    print("It applies the laws in the order: ACB" + color.END)
    time.sleep(5)
    print('')
    print(color.BOLD + "6-Va" + color.END)
    time.sleep(0.5)
    print(color.PURPLE + "Strenght: 350 kilos")
    time.sleep(0.5)
    print("Power: hydrogen")
    time.sleep(0.5)
    print("It applies the laws in the order: CAB" + color.END)
    time.sleep(5)
    print('')
    print(color.BOLD + "A-Numan" + color.END)
    time.sleep(0.5)
    print(color.PURPLE + "Strenght: 220 kilos")
    time.sleep(0.5)
    print("Power: atomic")
    time.sleep(0.5)
    print("It applies the laws in the order: CBA" + color.END)
    time.sleep(5)
    print('')
    print("These robots did have a motive for destroying V-Shnu, the company's budget has been cut.")
    time.sleep(5)
    print("Only four robots can be kept. V-Shnu's destruction gives its rivals greater chances of survival!")
    time.sleep(6)
    print('So the culprit could have broken Law B if it was to save itself as per Law C.')
    time.sleep(5)
    print('The tank was only half full, but it was enough to crush the little robot.')
    time.sleep(3.5)
    print("You could ask yourself, V-Shnu is fast - why didn't it flee?")
    time.sleep(3)
    print('Its enery comes from sunlight, so it was "idle" till morning.')
    time.sleep(4)
    print('')
    print("Who was the culprit? ")
    time.sleep(1)
    print("K-Li")
    time.sleep(0.5)
    print("Ga-Nesh")
    time.sleep(0.5)
    print("6-Va")
    time.sleep(0.5)
    print("A-Numan")
    time.sleep(0.5)
    print("Type 'exit' to exit")
    answer = input("> ")
    while answer != "6-Va" and answer != "exit":
        print(color.BOLD + "Wrong robot!!!")
        time.sleep(0.5)
        print(color.RED + "YOU LOOSE!!! 😧😧😧")
        # loop forever
        while True:
           time.sleep(10) 
    if answer != "exit":
        # display a helpful message
        print("You opened the safe and found a piece of paper...")
        # add the item to their inventory
        inventory.append("bucket")
        # delete the safe from the room
        del rooms[currentRoom]['safe']

def open1():
    print("Here is the story:")
    time.sleep(2)
    print('You are envestigating a case.')
    time.sleep(2)
    print('A titanium statue of only 2kg was on the desk in the office.')
    time.sleep(4)
    print('It vanished overnight.')
    time.sleep(2)
    print('A robot stole it.')
    time.sleep(2)
    print('The robots are on the first floor.')
    time.sleep(2)
    print('The office is on the second floor')
    time.sleep(2)
    print('The only way up is by the stairs')
    time.sleep(2)
    print('Here are the suspects:')
    time.sleep(2)
    print('')
    print(color.BOLD + "Moskito 5" + color.END)
    time.sleep(0.5)
    print(color.PURPLE + "Can flight and cary up to 3 kg." + color.END)
    time.sleep(5)
    print('')
    print(color.BOLD + "Spiderbot V3" + color.END)
    time.sleep(0.5)
    print(color.PURPLE + "Capable of climbing stairs and clearing 30cm obstacles.")
    time.sleep(0.5)
    print("Can lift up to 9kg with it's manibles" + color.END)
    time.sleep(5)
    print('')
    print(color.BOLD + "k-Terpillar" + color.END)
    time.sleep(0.5)
    print(color.PURPLE +"Can climb anything.")
    time.sleep(0.5)
    print("Transport capacity is 50% of Skara B's" + color.END)
    time.sleep(5)
    print('')
    print(color.BOLD + "Sakara B" + color.END)
    time.sleep(0.5)
    print(color.PURPLE + "Can move on fat ground only.")
    time.sleep(0.5)
    print("1.2m arm.")
    time.sleep(0.5)
    print("Transport capacity is 1kg less than Spiderbot's." + color.END)
    time.sleep(5)
    print('')
    print('The statue was hidden at the back of a locker, behind a 4kg drum.')
    time.sleep(4)
    print("Who was the thief? ")
    time.sleep(1)
    print("Moskito 5")
    time.sleep(0.5)
    print("Spiderbot V3")
    time.sleep(0.5)
    print("k-Terpillar")
    time.sleep(0.5)
    print("Skara B")
    time.sleep(0.5)
    print("Type 'exit' to exit")
    answer = input("> ")
    while answer != "K-Terpillar" and answer != "exit":
        print(color.BOLD + "Wrong robot!!!")
        time.sleep(0.5)
        print(color.RED + "YOU LOOSE!!! 😧😧😧")
        # loop forever
        while True:
           time.sleep(10) 
    if answer != "exit":
        # display a helpful message
        print("You opened the safe and found a piece of paper...")
        # add the item to their inventory
        inventory.append("bucket")
        # delete the safe from the room
        del rooms[currentRoom]['safe']


# A simple text adventure you can enhance with your own code

def showInstructions():
    # print a main menu and the commands
    print('\033[32m' + """
Text Adventure
==============
Commands:
  go [direction]
  get [item]
  show [item]
  use [item]
  search
  open safe
==============
Goal: Escape the house with the recipe
Avoid the monsters!
""" + color.END)

def showStatus():
    # print the player's current status
    print(color.ORANGE + "---------------------------")
    # show the player's current room
    print("You are in the " + currentRoom)
    # show the current inventory
    print("Inventory : " + str(inventory))
    # show the current effects of the room
    if 'effect' in rooms[currentRoom]:
        if 'dark' in rooms[currentRoom]['effect']:
            print("The room is dark, you can't see much")
        if 'light' in rooms[currentRoom]['effect']:
            print("The sun is going in your eyes, blocking your view")
        if 'fire' in rooms[currentRoom]['effect']:
            print(color.BOLD + "A " + color.RED + "fire" + color.ORANGE + color.BOLD + " is lit in the center of the room" + color.END)
    print("---------------------------" + color.END)

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    # FLOOR 1
    'Hall' : { 
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'north' : 'Bedroom'
        
    },

    'Kitchen' : {
        'west' : 'Living Room',
        'north' : 'Hall',
        'east' : 'Library',
        'animal' : 'monster',
        'safe' : 'recipe',
        'effect' : 'dark'
    },
    
    'Dining Room' : {
        'west' : 'Hall',
        'south' : 'Library',
        'item' : 'map'
    },
    
    'Library' : {
        'north' : 'Dining Room',
        'west' : 'Kitchen',
        'item' : 'book'
    },
        
    'Living Room' : {
        'east' : 'Kitchen',
        'north' : 'Locked Door',
        'west' : 'Red Bedroom',
        'safe' : 'torch'
    },
    
    'Bedroom' : {
        'south' : 'Hall',
        'west' : 'Small Bathroom',
        'item' : 'sunglasses',
    },
    
    'Small Bathroom' : {
        'east' : 'Bedroom',
        'item' : 'knife'
    },
    
    'Locked Door' : {
        'south' : 'Living Room'
    },
    
    
    # FLOOR 2
    'Red Bedroom' : { 
        'north' : 'Bathroom',
        'east' : 'Green Bedroom',
        'west' : 'Living Room',
        'safe' : 'paper2'
    },

    'Green Bedroom' : {
        'east' : 'Blue Bedroom',
        'south' : 'Closet',
        'west' : 'Red Bedroom',
        'animal' : 'monster',
        'safe' : 'paper4'
    },
    
    'Blue Bedroom' : { 
        'north' : 'Study',
        'east' : 'Yellow Bedroom',
        'west' : 'Green Bedroom',
        'safe' : 'paper1'
    },
    
    'Yellow Bedroom' : {
        'south' : 'Balcony',
        'west' : 'Blue Bedroom',
        'safe' : 'paper3'
    },
    
    'Bathroom' : {
        'south' : 'Red Bedroom',
        'item' : 'map2'
    },
    
    'Closet' : {
        'north' : 'Green Bedroom',
        'safe' : 'bucket',
        'effect' : 'dark'
    },
    
    'Balcony' : {
        'north' : 'Yellow Bedroom',
        'item' : 'paper',
        'effect': 'light'
    },
    
    'Study' : {
        'south' : 'Blue Bedroom',
        'safe' : 'key',
        'effect' : 'fire'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()
# loop forever
while True:
    showStatus()
    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

     # if they type 'open' first
    if move[0] == 'open':
        # if the second word is safe
        if move[1] == 'safe':
            # if there is a safe in the room
            if 'safe' in rooms[currentRoom]:
                # if the key is in the safe
                if 'key' in rooms[currentRoom]['safe']:
                    openSafeKey()
                    
                # if the torch is in the safe
                elif 'torch' in rooms[currentRoom]['safe']:
                    openSafeTorch()
                    
                # if the recipe is in the safe
                elif 'recipe' in rooms[currentRoom]['safe']:
                    openSafeRecipe()
                    
                # if the paper1 is in the safe
                elif 'paper1' in rooms[currentRoom]['safe']:
                    open1()
                    
                # if the paper2 is in the safe
                elif 'paper2' in rooms[currentRoom]['safe']:
                    open2()
                    
                # if the paper3 is in the safe
                elif 'paper3' in rooms[currentRoom]['safe']:
                    open3()
                    
                # if the paer4 is in the safe
                elif 'paper4' in rooms[currentRoom]['safe']:
                    open4()
                
                # if the bucket is in the safe
                elif 'bucket' in rooms[currentRoom]['safe']:
                    openSafeBucket()
            else:
                print("There is no safe in this room")



    # if they type 'go' first
    elif move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            if move[1] == 'west':
                if currentRoom == 'Red Bedroom':
                    print('You went down the stairs...')
                if currentRoom == 'Living Room':
                    print('You went up the stairs...')
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print("You can't go that way!")


    # if they type 'get' first
    elif move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            if move[1] == "map":
                # display a helpful message
                print("You got the the map of the ground floor!")
            elif move[1] == "map2":
                # display a helpful message
                print("You got the map of the first floor!")
            elif move[1] == "paper":
                # display a helpful message
                print("You got a piece of paper...")
            else:
                # display a helpful message
                print("You got the " + move[1] + "!")
            # delete the item from the room
            del rooms[currentRoom]['item']
        else:
            # if the item is not in the room
            print("You cannot get the " + move[1] + "!")
            
        
    # if they type 'search' first
    elif move[0] == 'search':
        # if the room has an effect
        if 'effect' in rooms[currentRoom]:
            if 'dark' in rooms[currentRoom]['effect']:
                # show room too dark if the room is too dark
                print("You cannot search well beacause the room is too dark")
            if 'light' in rooms[currentRoom]['effect']:
                # show room too light if the room is too light
                print("You cannot search well beacause the room is too light")
            if 'fire' in rooms[currentRoom]['effect']:
                # show room on fire if the room is on fire
                print("You cannot search well beacause of the smoke from the fire")
        else:
                # show an item if there is one
            if "item" in rooms[currentRoom]:
                print("You see a " + rooms[currentRoom]['item'])
                # show a safe is there is one
            elif "safe" in rooms[currentRoom]:
                print('You see a safe')
            else:
                # show no item if there is none
                print("You searched the room but didn't find anything")
            
            
    # if they type 'show' first
    elif move[0] == 'show':
        # if they contain the item they want to show
        if move[1] in inventory:
            if move[1] == "map":
                # display a helpful message
                print("Here is the map of the ground floor...")
            elif move[1] == "map2":
                # display a helpful message
                print("Here is the map of the first floor...")
            else:
                if move[1] in ["knife", "key", "book", "recipe", "torch", "paper1", "paper2", "paper3", "paper4", "paper"]:
                    # display a helpful message
                    print("Here is the " + move[1] + "...")
                else:
                    print("Sorry, we could not show you the " + move[1] + " 😢")
            # show their item
            if move[1] == 'knife':
                time.sleep(1)
                turtle.resetscreen()
                knife()
            elif move[1] == 'key':
                time.sleep(1)
                turtle.resetscreen()
                key()
            elif move[1] == 'map':
                time.sleep(1)
                turtle.resetscreen()
                Map()
            elif move[1] == 'map2':
                time.sleep(1)
                turtle.resetscreen()
                Map2()
            elif move[1] == 'book':
                time.sleep(1)
                turtle.resetscreen()
                book()
            elif move[1] == 'recipe':
                time.sleep(1)
                recipe()
            elif move[1] == 'torch':
                time.sleep(1)
                turtle.resetscreen()
                torch()
            elif move[1] == 'paper1':
                time.sleep(1)
                turtle.resetscreen()
                paper1()
            elif move[1] == 'paper2':
                time.sleep(1)
                turtle.resetscreen()
                paper2()
            elif move[1] == 'paper3':
                time.sleep(1)
                turtle.resetscreen()
                paper3()
            elif move[1] == 'paper4':
                time.sleep(1)
                turtle.resetscreen()
                paper4()
            elif move[1] == 'paper':
                time.sleep(1)
                turtle.resetscreen()
                paper()
        else:
            # if the item is not in their inventory
            print("You do not have the " + move[1] + "!")
            
            
        # if they type 'use' first
    elif move[0] == 'use':
        # if they have the item they want to use
        if move[1] in inventory:
            # if the room has an effect
            if 'effect' in rooms[currentRoom]:
                # if the item is a torch
                if move[1] == 'torch':
                    # if room is dark
                    if 'dark' in rooms[currentRoom]['effect']:
                        # remove the dark
                        del rooms[currentRoom]['effect']
                        # display a helpful message
                        print("The room is lit")
                        print("You can now search")
                    else:
                        # display a helpful message
                        print("The room is already lit!")
                            # if the item is a torch
                # if the item is a sunglasses
                if move[1] == 'sunglasses':
                    # if room is dark
                    if 'light' in rooms[currentRoom]['effect']:
                        # remove the dark
                        del rooms[currentRoom]['effect']
                        # display a helpful message
                        print("You put on your sunglasses, you can see better")
                        print("You can now search")
                    else:
                        # display a helpful message
                        print("You already have sunglasses on!")
                            # if the item is a torch
                if move[1] == 'bucket':
                    # if room is dark
                    if 'fire' in rooms[currentRoom]['effect']:
                        # remove the dark
                        del rooms[currentRoom]['effect']
                        # display a helpful message
                        print("You put off the fire")
                        print("You can now search")
                    else:
                        # display a helpful message
                        print("There is no fire in the room!")
            else:
                # if they cannot use the item
                print("You cannot use the " + move[1] + "!")
        else:
            # if the item is not in their inventory
            print("You do not have the " + move[1] + "!")
            
            
    # if they type 'hack' first     
    elif move[0] == 'hack':
        # if they type 'get' second
        if move[1] == 'get':
            # add the item to their inventory
            inventory += [move[2]]
            # display a helpful message
            print("You got the " + move[2] + "!")
        # if they type 'go' second   
        if move[1] == 'go':
            # if they type 'hall' third  
            if move[2] == 'hall':
                # set current room to the hall
                currentRoom = 'Hall'
                # display a helpful message
                print('You got teleported back to the Hall')
            # if they type 'red' third
            if move[2] == 'red':
                # set current room to the red bedroom
                currentRoom = 'Red Bedroom'
                # display a helpful message
                print('You got teleported to the Red Bedroom')
    
    # the user did not input a valid command
    else:
        print("This is not a valid command")
    
    # player looses if they enter a room with a monster
    if 'animal' in rooms[currentRoom]:
        if 'monster' in rooms[currentRoom]['animal']:
            if currentRoom == 'Kitchen':
                print('A monster is in the kitchen')
                print("Type 'exit' to go back to the hall")
                answer = input(">")
                if answer != "exit":
                    # if they type use knife
                    if answer == "use knife":
                        # if they have a knife
                        if 'knife' in inventory:
                            print('You manage to kill the monster with your knife.')
                            del rooms[currentRoom]['animal']
                        else:
                            print (color.BOLD + color.RED + 'A monster has got you... GAME OVER!😧😧😧')
                            break
                    else:
                        print (color.BOLD + color.RED + 'A monster has got you... GAME OVER!😧😧😧')
                        break
                else:
                    print("You were teleported back to the hall")
                    currentRoom = 'Hall'
            else:
                print('A monster is in the Green Bedroom')
                print("Type 'exit' to go back to the Red Bedroom")
                answer = input(">")
                if answer != "exit":
                    # if they type use knife
                    if answer == "use knife":
                        # if they have a knife
                        if 'knife' in inventory:
                            print('You manage to kill the monster with your knife.')
                            del rooms[currentRoom]['animal']
                        else:
                            print (color.BOLD + color.RED + 'A monster has got you... GAME OVER!😧😧😧')
                            break
                    else:
                        print (color.BOLD + color.RED + 'A monster has got you... GAME OVER!😧😧😧')
                        break
                else:
                    print("You were teleported back to the Red Bedroom")
                    currentRoom = 'Red Bedroom'
            
        
    # check if it player is in the locked door
    if currentRoom == 'Locked Door':
        if 'key' in inventory:
            # player wins if they escapes with the recipe
            if 'recipe' in inventory:
                print(color.BOLD + color.GREEN + 'You escaped the house... YOU WIN!!! 🏆😃😃😃🏆')
                time.sleep(1)
                snowflake()
                break
            # player looses if they escapes without the recipe
            else:
                print('You escaped the house...')
                time.sleep(1)
                print('The door closes itself...')
                time.sleep(1)
                print('You are stuck outside, and without the recipe...')
                time.sleep(1)
                print(color.BOLD + color.RED + 'YOU LOOSE!!! 😧😧😧')
                break
        # player does not have the key
        else:
            print("The door is locked, you need a key to open it.")
            currentRoom = 'Living Room'
