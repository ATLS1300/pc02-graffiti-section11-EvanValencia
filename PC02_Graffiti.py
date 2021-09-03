#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

turtle.penup()
turtle.goto(20,80)
turtle.pencolor("red")
turtle.dot(40)
turtle.goto(-15,92)
turtle.pencolor("cyan")
turtle.pendown()
turtle.left(90)
turtle.pensize(5)
turtle.begin_fill()
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.fillcolor("cyan")
turtle.end_fill()
turtle.penup()
turtle.goto(35,110)
turtle.pensize(2)
turtle.pendown()
turtle.begin_fill()
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.end_fill()









   



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
