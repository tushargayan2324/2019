#!/usr/bin/python


def f(n):
 if n==0:
  return 1
 elif n==1:
  return 1
 elif n>=2:
  return n*f(n-1)
   
n=input("Enter a number:")
print(f(n))
