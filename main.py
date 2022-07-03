import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")

def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        tim.color(random_color())
        tim.circle(90)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_graph)

draw_spirograph(5)
screen = Screen()
screen.exitonclick()
