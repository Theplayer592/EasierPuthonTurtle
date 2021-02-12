import turtle #Import turtle

t = turtle.Turtle() #Declare turtle variable

def fd(i):
    t.forward(i)

def bk(i):
    t.back(i)

def rt(i):
    t.right(i)

def lt(i):
    t.left(i)

def drawShape(sides = 4, size = 10, increaseSize = 0, reps = 1, Hex = "#000000"):
    t.pencolor(Hex)
    for timesDrawn in range(reps):
        for sidesDrawn in range(sides):
            fd(size)
            lt(360/sides)
        size += increaseSize
        
def drawAvLogo(size = 10, speed = 0, Hex = "#000000"):
    reps = 0
    shapeSides = 370
    exteriorAngle = 1

    t.speed(speed) #Set this to whatever you want
    t.pensize(size) #The thickness of the lines
    t.color(Hex) #The color of the pen (at start)

    #Makes the circle (would be quicker in js)
    while reps < shapeSides: #Set 5 to the number of sides the shape has
      t.forward(1)
      t.right(exteriorAngle) #The external angle of the shape
      reps += 1

    #Make the A
    t.right(80)
    t.forward(85)
    t.right(180)
    t.forward(95)
    t.right(180)
    t.forward(95)
    t.right(180)
    t.forward(15)
    t.left(90)
    t.forward(45)
    t.right(118)
    t.forward(91)
    t.right(180)
    t.forward(140)
    
    #Make the arrow on the A
    t.right(180)
    t.forward(45)
    t.right(62)
    t.forward(45)
    t.pencolor('white') #Change the color of the drawing for the arrow's border only
    t.left(135)
    t.forward(20)
    t.right(180)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.pencolor(Hex)
    t.pensize(size/2)
    t.right(180)
    t.forward(20)
    t.left(90)
    t.forward(20)
    
    #Make the arrow's root clearer
    t.right(180)
    t.forward(20)
    t.right(505)
    t.penup()
    t.forward(7)
    t.pendown()
    t.pensize(size*1.2)
    t.pencolor(Hex)
    t.forward(10)
    
    #Hide the turtle
    t.ht()
