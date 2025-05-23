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

#Set speed variable
speed = 1

#Define functions

def turnleft():
    player.left(30)

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")



while True:
    player.forward(speed)









delay = input("Press Enter to finish")








