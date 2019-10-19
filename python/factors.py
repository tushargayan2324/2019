#!/usr/bin/python


def factors(n):
        for i in range(2,n):
            if n%i==0:
                print(i)

m = input("Enter ")

print(factors(m))
