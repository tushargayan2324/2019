#!/usr/bin/python

import turtle

t = turtle

side = 300
n = 3

def polygon(s, n):
    for i in range(n):
        t.forward(s)
        t.left(360/n)

i = 1
while True:
    t.fillcolor(1 - (1.0/i), 1/(i), 10**(-i))
    t.begin_fill()
    polygon(side / i, n)
    t.end_fill()
    t.left(180 - 360/n)
    i += 1

turtle.exitonclick()
