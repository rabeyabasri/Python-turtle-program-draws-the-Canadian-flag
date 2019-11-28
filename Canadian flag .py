import turtle

screen = turtle.Screen()
myTurtle = turtle.Turtle()

#starting point
myTurtle.penup
myTurtle.color("white")
myTurtle.goto(-300,300)
myTurtle.pendown


#drawing the pole
myTurtle.color("silver", "silver")
myTurtle.begin_fill()

myTurtle.right(90)
myTurtle.forward(800)
myTurtle.right(90)
myTurtle.forward(10)
myTurtle.right(90)
myTurtle.forward(800)
myTurtle.right(90)
myTurtle.forward(10)

myTurtle.end_fill()


def flagPart(width, legth, color, fill):
    myTurtle.color(color, fill)
    myTurtle.begin_fill()
    myTurtle.forward(legth)
    myTurtle.pendown
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(legth)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(legth)
    myTurtle.end_fill()
    
    
#Parts of the flag
flagPart(200, 100, "red", "red")
flagPart(200, 200, "black", "white")
flagPart(200, 100, "red", "red")

#moving turtle to the centre
myTurtle.right(90)
myTurtle.penup()
myTurtle.forward(200)
myTurtle.right(90)
myTurtle.forward(200)
myTurtle.right(90)
myTurtle.forward(30)
#print(myTurtle.position())

#angle function
def drawAngle(l1, l2, degree):
    myTurtle.forward(l1)
    myTurtle.right(180-degree)
    myTurtle.forward(l2)

def leafPart(l1, l2, l3, l4, l5, l6, cangle1,cangle2,cangle3, a1, a2, a3):
    #Angle1
    myTurtle.left(a1)
    drawAngle(l1,l2,cangle1)

    #Angle2
    myTurtle.left(a2)
    drawAngle(l3,l4,cangle2)

    #Angle3
    myTurtle.left(a3)
    drawAngle(l5,l6,cangle3)

#drawing maple data
myTurtle.pendown()
myTurtle.left(90)
myTurtle.forward(2.5)
myTurtle.right(90)
myTurtle.forward(15)

#drwaing the leaf(repeat from here)

myTurtle.color("red", "red")
myTurtle.begin_fill()

#lower angle
myTurtle.left(100)
drawAngle(40,15,60)

#three angles
def leafPart(l1, l2, l3, l4, l5, l6, cangle1,cangle2,cangle3, a1, a2, a3):
    #Angle1
    myTurtle.left(a1)
    drawAngle(l1,l2,cangle1)

    #Angle2
    myTurtle.left(a2)
    drawAngle(l3,l4,cangle2)

    #Angle3
    myTurtle.left(a3)
    drawAngle(l5,l6,cangle3)

leafPart(50,15,30,30,15,40,60,60,60,75,90,75)

#first angle of the uper leaf part
myTurtle.left(165)
drawAngle(60,20, 40)

myTurtle.left(120)
#print(myTurtle.position())

#top line
myTurtle.goto(-100,280)
myTurtle.goto(-100,130)

myTurtle.end_fill()

#2nd half..............................................................

def drawAngle2(l1, l2, degree):
    myTurtle.forward(l1)
    myTurtle.left(180-degree)
    myTurtle.forward(l2)
    
#turning to the opposite side
myTurtle.right(90)

myTurtle.color("red", "red")
myTurtle.begin_fill()

#2nd half of the data
myTurtle.forward(2.5)
myTurtle.left(90)
myTurtle.forward(15)

#lower angle
myTurtle.right(100)
drawAngle2(40,15,60)

#three angles
def leafPart2(l1, l2, l3, l4, l5, l6, cangle1,cangle2,cangle3, a1, a2, a3):
    #Angle1
    myTurtle.right(a1)
    drawAngle2(l1,l2,cangle1)

    #Angle2
    myTurtle.right(a2)
    drawAngle2(l3,l4,cangle2)

    #Angle3
    myTurtle.right(a3)
    drawAngle2(l5,l6,cangle3)

leafPart2(50,15,30,30,15,40,60,60,60,75,90,75)

#first angle of the uper leaf part
myTurtle.right(165)
drawAngle2(60,20, 40)

myTurtle.right(120)
#print(myTurtle.position())

#top line
myTurtle.goto(-100,280)


myTurtle.end_fill()

myTurtle.color("white")

myTurtle.listen()

myTurtle.onkey("Enter")












    












