from turtle import *

def draw_square():
    color("yellow")
    length = 100
    for i in range(4):
        forward(length)
        left(90)

draw_square()