#Turtle Graphic Game 
import turtle

#Set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

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









delay = input("Press Enter to finish")








