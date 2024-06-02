#!/bin/python3

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
    pat.forward(250)
    left()
    pat.forward(200)
    left()
    pat.forward(112.5)
    door()
    pat.forward(112.5)
    pat.end_fill()

    pat.hideturtle()


# Recipe
def recipe():
    print("Vanilla Cake")
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
    print("=============================================================================================================================================================================================================")
    time.sleep(1)


# Phone Number Challenge
def phoneNumberChallenge():
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


# Open safe function
def openSafeKey():
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


def openSafeRecipe():
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
        
        
def openSafeTorch():
    # clear screen
    turtle.resetscreen()
    print("The password contains 4 numbers, it is hidden somewhere in the game")
    print('Type "exit" to exit')
    answer = input("What is the password? ")
    while answer != "1986" and answer != "exit":
        print("Wrong password - try again!")
        answer = input("What is the password? ")
    if answer == "1986":
        # display a helpful message
        print("You opened the safe and found a " + rooms[currentRoom]['safe'] +"!")



# A simple text adventure you can enhance with your own code

def showInstructions():
    # print a main menu and the commands
    print("""
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
""")
# opposite directions
direction1 = ["north", "south", "east", "west"]
direction2 = ["south", "north", "west", "east"]

def showStatus():
    # print the player's current status
    print("---------------------------")
    print("You are in the " + currentRoom)
    # show the current inventory
    print("Inventory : " + str(inventory))
    if 'dark' in rooms[currentRoom]:
        print("The room is dark, you can't see much")
    print("---------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

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
        'dark' : 'dark'
    },
    
    'Dining Room' : {
        'west' : 'Hall',
        'south' : 'Library',
        'item' : 'torch'
    },
    
    'Library' : {
        'north' : 'Dining Room',
        'west' : 'Kitchen',
        'item' : 'book'
    },
        
    'Living Room' : {
        'east' : 'Kitchen',
        'north' : 'Locked Door',
        'safe' : 'knife'
    },
    
    'Bedroom' : {
        'south' : 'Hall',
        'west' : 'Bathroom',
        'safe' : 'key',
    },
    
    'Bathroom' : {
        'east' : 'Bedroom',
        'item' : 'map'
    },
    
    'Locked Door' : {
        'south' : 'Living Room'
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
                    # add the item to their inventory
                    inventory.append("key")
                    # delete the safe from the room
                    del rooms[currentRoom]['safe']
                    
                # if the torch is in the safe
                elif 'torch' in rooms[currentRoom]['safe']:
                    openSafeTorch()
                    # add the item to their inventory
                    inventory.append("torch")
                    # delete the safe from the room
                    del rooms[currentRoom]['safe']
                    
                # if the recipe is in the safe
                elif 'recipe' in rooms[currentRoom]['safe']:
                    openSafeRecipe()
                    # add the item to their inventory
                    inventory.append("recipe")
                    # delete the safe from the room
                    del rooms[currentRoom]['safe']
                    
            else:
                print("There is no safe in this room")



    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print("You can't go that way!")


    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print("You got the " + move[1] + "!")
            # delete the item from the room
            del rooms[currentRoom]['item']
        else:
            # if the item is not in the room
            print("You cannot get the " + move[1] + "!")
            
        
    # if they type 'search' first
    if move[0] == 'search':
        if 'dark' in rooms[currentRoom]:
            # show room too dark if the room is too dark
            print("You cannot search well beacause the room is too dark")
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
    if move[0] == 'show':
        # if they contain the item they want to show
        if move[1] in inventory:
            # display a helpful message
            print("Here is the " + move[1] + "...")
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
            else:
                print("Sorry, we could not show you the " + move[1] + " 😢")
        else:
            # if the item is not in their inventory
            print("You do not have the " + move[1] + "!")
            
            
        # if they type 'use' first
    if move[0] == 'use':
        # if they have the item they want to use
        if move[1] in inventory:
            # if they can use the item
            if move[1] == 'torch':
                # if room is dark
                if 'dark' in rooms[currentRoom]:
                    # remove the dark
                    del rooms[currentRoom]['dark']
                    # display a helpful message
                    print("The room is lit")
                    print("You can now search")
                else:
                    # display a helpful message
                    print("The room is already lit!")
            else:
                # if they cannot use the item
                print("You cannot use the " + move[1] + "!")
        else:
            # if the item is not in their inventory
            print("You do not have the " + move[1] + "!")
            
            
    # if they type 'hack' first     
    if move[0] == 'hack':
        # if they type 'get' second
        if move[1] == 'get':
            # add the item to their inventory
            inventory += [move[2]]
            # display a helpful message
            print("You got the " + move[2] + "!")
        
        
    # player looses if they enter a room with a monster
    if 'animal' in rooms[currentRoom]:
        if 'monster' in rooms[currentRoom]['animal']:
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
                        print ('A monster has got you... GAME OVER!😧😧😧')
                        break
                else:
                    print ('A monster has got you... GAME OVER!😧😧😧')
                    break
            else:
                print("You were teleported back to the hall")
                currentRoom = 'Hall'
        
        
        
    # check if it player is in the locked door
    if currentRoom == 'Locked Door':
        if 'key' in inventory:
            # player wins if they escapes with the recipe
            if 'recipe' in inventory:
                print('You escaped the house... YOU WIN!🏆😃😃😃🏆')
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
                print('YOU LOOSE!😧😧😧')
                break
        # player does not have the key
        else:
            print("The door is locked, you need a key to open it.")
            currentRoom = 'Living Room'
            
            
            
