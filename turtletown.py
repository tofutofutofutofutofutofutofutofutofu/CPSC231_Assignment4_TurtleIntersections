# Class: CPSC 231 L02
# Name: Christopher Lee
# Tutorial 10
# ID:10136117
# Date: November 26, 2020
# This code does what is outlined in Assignment 4: turtle intersections

import turtle
import math

# Constant Declaration
WIDTH = 800
HEIGHT = 600
HALFWIDTH = 400
HALFHEIGHT = 300
INTERSECTRADIUS = 5

# SETUP
mrTurtle = turtle.Turtle()
mrTurtle.shape("turtle")
screen = mrTurtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

# Getting the coordinates for circle, line and radius
xc = int(input("Enter circle x coordinate:"))
yc = int(input("Enter circle y coordinate:"))
r = float(input("Enter radius of circle:"))
x1 = int(input("Enter line start x coordinate:"))
y1 = int(input("Enter line start y coordinate:"))
x2 = int(input("Enter line end x coordinate:"))
y2 = int(input("Enter line end y coordinate:"))
# Counter for real intersections
counter = 0
endings = {0: "No Intersect!", 1: "One Intersect!", 2: "Two Intersect!"}

# Math stuff that does something: d is stuff under square root for quadratic
a = (x2 - x1) ** 2 + (y2 - y1) ** 2
b = 2 * ((x1 - xc) * (x2 - x1) + (y1 - yc) * (y2 - y1))
c = (x1 - xc) ** 2 + (y1 - yc) ** 2 - r ** 2
d = b ** 2 - 4 * a * c

# Draw Axis
mrTurtle.penup()
mrTurtle.goto(0, HALFHEIGHT)
mrTurtle.pendown()
mrTurtle.goto(WIDTH, HALFHEIGHT)
mrTurtle.goto(HALFWIDTH, HALFHEIGHT)
mrTurtle.goto(HALFWIDTH, 0)
mrTurtle.goto(HALFWIDTH, HEIGHT)
mrTurtle.penup()
# Draw Circle
mrTurtle.color("red")
mrTurtle.goto(xc, yc - r)
mrTurtle.pendown()
mrTurtle.circle(r)
mrTurtle.penup()
# Draw Lines
mrTurtle.color("blue")
mrTurtle.goto(x1, y1)
mrTurtle.pendown()
mrTurtle.goto(x2, y2)
mrTurtle.penup()
# Draw text and intersects
mrTurtle.color("green")


# This function will draw circles around intersections given the x and y coordinates)
def drawintersect(xcord, ycord):
    mrTurtle.goto(xcord, ycord - INTERSECTRADIUS)
    mrTurtle.pendown()
    mrTurtle.circle(INTERSECTRADIUS)
    mrTurtle.penup()


if d > 0:
    # Math stuff to find intersect coordinates
    alpha1 = ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    alpha2 = ((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    intersect1x = (1 - alpha1) * x1 + alpha1 * x2
    intersect1y = (1 - alpha1) * y1 + alpha1 * y2
    intersect2x = (1 - alpha2) * x1 + alpha2 * x2
    intersect2y = (1 - alpha2) * y1 + alpha2 * y2
    # Check for real intersections not infinity line
    if 1 >= alpha1 >= 0:
        drawintersect(intersect1x, intersect1y)
        counter += 1
    # This one makes it skip 2 if it's the same value: aka one intersect
    if alpha1 == alpha2:
        alpha2 = 2
    if 1 >= alpha2 >= 0:
        drawintersect(intersect2x, intersect2y)
        counter += 1

mrTurtle.goto(HALFWIDTH, HALFHEIGHT + 100)
style = ('Courier', 50)
mrTurtle.write(endings.get(counter), font=style, align='center')
turtle.done()
