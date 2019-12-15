#!/usr/bin/python

#def universal time and time step(accuracy of graph)
uni_time = 0
time_step = 0.001
t = uni_time

#initial conditions
vel = [0,0,0]
pos = [1,2,1]

#give acceleration as function of time
def acc(time):
    return [time,time**2,1]

#input for time
time = input("Time ")

#def current attributes of the particle
for j in range(int(float(time)/time_step)):
    print(pos)
    for i in range(3):
        vel[i] = vel[i] + acc(t)[i]*time_step
        pos[i] = pos[i] + vel[i]*time_step
    t = t + time_step
    for i in range(3):
        acc(t)[i] = acc(t)[i]
