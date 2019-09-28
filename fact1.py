#!/usr/bin/python

import time

def fact(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f

b=input("Enter ")

start_time = time.time()

f = fact(b)

stop_time = time.time()

print(f)
print("--- %s seconds ---" % (stop_time - start_time))


