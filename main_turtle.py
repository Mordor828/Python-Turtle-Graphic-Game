#Turtle Graphic Game 
import turtle
import math

#Set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

#Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()


#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

#Create goal
goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-100,-100)


#Set speed variable
speed = 1

#Define functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
     global speed
     speed += 1


#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")



while True:
    player.forward(speed)

    #boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    
    #boundary Checking
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)




    


    









delay = input("Press Enter to finish")








