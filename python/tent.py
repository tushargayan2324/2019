#!/usr/bin/python

import math

def f(n):
    l = int(math.sqrt(n))
    for i in range(2,l):
        if l%i==0:
            print(i)
            
            
print(f(9))
    
    
