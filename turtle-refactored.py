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
    polygon(t, size, 4)

# Draw a circle. Parameters:
#   t: A Turtle object
#   radius: The radius of the circle
def circle(t, radius):
    circumference = 2 * math.pi * radius
    num_sides = 100
    length = circumference / num_sides
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
