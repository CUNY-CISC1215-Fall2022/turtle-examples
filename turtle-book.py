# This file contains the refatored and cleaned up turtle
# shape library example we completed in class. The comments
# contain descriptions of the functions, along with notes
# related to how the code was refactored.
#
# Please note: The book's approach did things a little different than
# we did in class. The book's turtle turns left instead of right,
# and uses some Turtle function shorthand (fd() instead of forward()).
# However, it is all fundamentally the same.
#
# For the best experience in seeing software development involving
# writing code, encapsulation, generalization, and refactoring,
# you should try following along with this yourself - the book
# and the lecture slides contain the entire process. Studying this code
# by itself won't show you the process.

import math
import turtle

my_turtle = turtle.Turtle()

# Low-level shape functions
# =========================

# Draw a polyline. A polyline is made by repeatedly moving the turtle
# by some amount, then rotating it by some angle. The number of times
# the turtle moves is controllable, so this function can produce both
# open and closed shapes.
# Parameters:
#   t: A Turtle object
#   n: The number of sides to draw
#   length: The length of each side of the polyline
#   angle: The angle between each side
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# Draw an arc. An arc is a portion of a circle. This function can be
# used to draw an open arc (angle < 360) or a closed circle (angle = 360).
# Parameters:
#   t: A Turtle object
#   r: The radius of the arc
#   angle: The amount of the arc to draw
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360

    # This is a neat trick that lets us vary the number of straight lines
    # we draw so it is proportional to the length of the arc.
    n = int(arc_length / 3) + 1

    step_length = arc_length / n
    step_angle = angle / n
    # A circle is just a closed polyline with many sides. We can use the
    # existing polyline function instead of rewriting its loop here
    polyline(t, n, step_length, step_angle)


# High-level shape functions
# ==========================

# Draw a polygon. Parameters:
#   t: A Turtle object
#   n: The number of sides
#   length: The length of each side
def polygon(t, n, length):
    angle = 360.0 / n
    # A polygon is just a closed polyline. We can use the existing
    # polyline function instead of rewriting its loop here
    polyline(t, n, length, angle)


# Draw a square. Parameters:
#   t: A Turtle object
#   size: The length of each side of the square
def square(t, size):
    # No need to replicate the square drawing code here:
    # a square is just a 4-sided polygon, so there is
    # no need to replicate the loop here: reuse the
    # polygon() function instead.
    polygon(t, 4, size)

# Draw a circle. Parameters:
#   t: A Turtle object
#   radius: The radius of the circle
def circle(t, radius):
    # A circle is just a 360-degree arc, so there is no need
    # to replicate the loop code here: reuse the arc()
    # function instead.
    arc(t, radius, 360)

# Give the turtle drawing instructions
circle(my_turtle, 15)
my_turtle.up()
my_turtle.left(45)
my_turtle.forward(100)
my_turtle.down()
square(my_turtle, 200)
my_turtle.left(90)
polygon(my_turtle, 8, 75)

turtle.mainloop()
