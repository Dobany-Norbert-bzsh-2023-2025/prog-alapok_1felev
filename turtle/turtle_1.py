import turtle as t
from random import random, randint
""""
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)

color('green')
fillcolor('yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
"""
import turtle
import random

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed (0 is the fastest)

# Function to draw a random pattern
def random_pattern():
    for _ in range(100):
        angle = random.randint(0, 360)  # Choose a random angle between 0 and 360 degrees
        t.setheading(angle)  # Set the Turtle's heading
        t.forward(50)  # Move the Turtle forward by 50 units

# Main loop to draw the random pattern
for _ in range(4):  # You can change the number of patterns drawn
    random_pattern()

# Close the Turtle graphics window when clicked
screen.exitonclick()


        