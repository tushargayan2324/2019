#!/usr/bin/python

from os import sys

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

for i in range(0,n):
 print fib(int(sys.argv[1]))
