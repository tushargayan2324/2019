#!/usr/bin/python

def lucasno(n):
    if n==1:
        return 4
    else:
        return (lucasno(n-1))**2 - 2

def mersenneprime(n):
    a = n
    i = 1
    
    if a > lucasno(i):
        i = i + 1
    
    elif a <= lucasno(i):
        remainder = lucasno(i)%n
        a = remainder
        
    elif a == 0:
        return n
    
    else:
        print("Not prime ")
        
            
m = input('Prime no check: ')

print(mersenneprime(m))
