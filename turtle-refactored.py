# This file contains the refatored and cleaned up turtle
# shape library example we completed in class. The comments
# contain descriptions of the functions, along with notes
# related to how the code was refactored.
#
# For the best experience in seeing software development involving
# writing code, encapsulation, generalization, and refactoring,
# you should try following along with this yourself - the book
# and the lecture slides contain the entire process.

import math
import turtle

my_turtle = turtle.Turtle()

# Draw a polygon. Parameters:
#   t: A Turtle object
#   size: The length of each side of the polygon
#   sides: The number of sides of the polygon
def polygon(t, size, sides):
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.right(angle)

# Draw a square. Parameters:
#   t: A Turtle object
#   size: The length of each side of the square
def square(t, size):
    # No need to replicate the square drawing code here:
    # a square is just a 4-sided polygon, so there is
    # no need to replicate the loop here: reuse the
    # polygon() function instead.
    polygon(t, size, 4)

# Draw a circle. Parameters:
#   t: A Turtle object
#   radius: The radius of the circle
def circle(t, radius):
    circumference = 2 * math.pi * radius
    num_sides = 100
    length = circumference / num_sides
    # A circle is just a many-sided polygon with
    # length decided by the math above. No need to
    # replicate the loop here: reuse the polygon()
    # function instead.
    polygon(t, length, num_sides)

# Give the turtle drawing instructions
circle(my_turtle, 15)
my_turtle.up()
my_turtle.left(45)
my_turtle.forward(100)
my_turtle.down()
square(my_turtle, 200)
my_turtle.left(90)
polygon(my_turtle, 75, 8)

turtle.mainloop()
