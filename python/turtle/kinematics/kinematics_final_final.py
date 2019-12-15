#!/usr/bin/python

"""***Tushar Gayan***
   Give the acc in 3 dimension and it will give a data.txt file as set of points that can be plotted
   Vary the accuracy of graph by setting time_steps
"""

import math

#def universal time and time step(accuracy of graph)
uni_time = 0
time_step = 0.001
t = uni_time

#initial conditions
vel = [0,0,0]
pos = [1,2,1]

#give acceleration as function of time
def acc(t):
    return [math.log(t+1),math.e**(t),1]

#input for time
time = input("Time ")

#writing data(opening file)
data = open('data.txt' , 'w')

#def current attributes of the particle
for j in range(int(float(time)/time_step)):
    print(pos)
    data.write("%.14f\t%.14f\t%.14f\n" %(pos[0],pos[1],pos[2]))
    for i in range(3):
        vel[i] = vel[i] + acc(t)[i]*time_step
        pos[i] = pos[i] + vel[i]*time_step
    t = t + time_step
    for i in range(3):
        acc(t)[i] = acc(t)[i]
