#!/usr/bin/python

import time

def fib2(n):
    i=0
    a=0
    b=1
    while i < n: 
        a,b = b, a+b
        i+=1
        print(a)


l=input("Enter ")

start_time=time.time()
f=fib2(l)
stop_time=time.time()

print(f)
print("---%s seconds ---"%(stop_time-start_time))
