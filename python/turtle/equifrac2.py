#!/usr/bin/python

import turtle
import math

def frac2(side):
    turtle.speed('fastest')
    i = 2    
    while True:
        turtle.forward(side/i)
        turtle.left(120)
        turtle.forward(side/i)
        turtle.left(120)
        turtle.forward(side/i)
        turtle.left(120)
        turtle.left(10)
        i = i + 1
        
frac2(600)
