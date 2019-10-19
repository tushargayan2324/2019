#!/usr/bin/python

import random
import math

def random_walk1(n):
    l = [-1,0,1]
    x = 0
    dist = 0
    for i in range(1,n+1):
            m = random.choice(l)
            x = x + m
            dist = dist + abs(m)
            avgdist = float(dist)/i
            print(i,x,dist,avgdist)

m = input("Number of steps ")

random_walk1(m)

