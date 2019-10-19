#!/usr/bin/python
import turtle
import random
t2=turtle.Turtle()
turtle.speed('fastest')
def snowflake(n):
 turtle.speed('fastest')
 t2.penup()
 t2.forward(10*n)
 t2.left(45)
 t2.pendown()
 for i in range(8):
  branch(n)
  t2.left(45)

def branch(n):
 turtle.speed('fastest')
 for i in range(3):
  for i in range(3):
   t2.forward(10.0*n/3)
   t2.backward(10.0*n/3)
   t2.right(45)
  t2.left(90)
  t2.backward(10.0*n/3)
  t2.left(45)
 t2.right(90)
 t2.forward(10.0*n)
 
for i in range(20):
 x=random.randint(-200,200)
 y=random.randint(-200,200)
 sf_n=random.randint(1,4)
 t2.penup()
 t2.goto(x,y)
 t2.pendown()
 snowflake(sf_n)

