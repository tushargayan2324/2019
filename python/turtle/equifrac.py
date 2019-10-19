#!/usr/bin/python

import turtle

t=turtle

side=500


i=1
while True:
 t.forward(side/(2**i))
 t.left(120)
 t.forward(side/(2**i))
 t.left(120)
 t.forward(side/(2**i))
 t.left(120)
 t.forward(side/(2**(i+1)))
 i=i+1
