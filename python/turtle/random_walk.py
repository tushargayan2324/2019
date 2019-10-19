#!/usr/bin/python

import random
import turtle

l = range(0, 360, 1)

def random_walk(side):
    turtle.speed('fastest')
    c = 1
    ld = []
    turtle.showturtle()
    while True:
        m = random.choice(l)
        turtle.forward(side)
        turtle.left(m)
        d = turtle.distance(0, 0) / side
        ld.append(c / d**2)
        print c, d, c / d**2, sum(ld) / c
        c += 1
    
random_walk(5)
