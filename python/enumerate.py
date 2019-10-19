#!/usr/bin/python

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
        
l=range(100)

enumerate(l,start=0)

