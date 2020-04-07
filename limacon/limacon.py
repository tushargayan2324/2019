from math import pi
import sys

num_dots = 500 #Number of dots on the edge of circle

radius = 5

multiplier = float(sys.argv[1])

points  = {}

for i in range(num_dots):
    points[i] = ( (i*multiplier/40) % num_dots)   #change the multiplier's divisor for intermediate frames

dat_file = open("limacon_dat.txt" , "w")

def theta(k):
    return float(2*k*pi)/num_dots

for i in range(num_dots):
    dat_file.write("%.16f\t%f\n"%( theta(i)  , radius ))
    dat_file.write("%.16f\t%f\n"%( theta(points[i])  , radius ))
    
dat_file.close()
