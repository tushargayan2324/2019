#!/usr/bin/python
import turtle
turtle.showturtle()

side = 600
def frac1(side):
     turtle.speed('fastest')
     i = 2
     while True:
             turtle.forward(side/i)
             turtle.left(90)
             turtle.forward(side/i)
             turtle.left(90)
             turtle.forward(side/i)
             turtle.left(90)
             turtle.forward(side/i)
             turtle.left(90)
             turtle.left(10)
             i = i + (1.0/2)**i
 
frac1(side)
