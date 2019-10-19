#!/usr/bin/python


import turtle

def frac(n):
    c = 0
    while True:
        turtle.forward(n/2**c)
        turtle.left(120)
        turtle.forward(n/2**c)
        turtle.left(120)
        turtle.forward(n/2**c)
        turtle.left(120)
        turtle.forward(n/2**(c+1))
        turtle.left(60)
        c = c + 1
        
frac(500)
