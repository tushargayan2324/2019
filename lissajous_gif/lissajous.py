
import math,sys

A_x = 1
A_y = 1
#A_z = 6

w_x = 4
w_y = 8
#w_z = 9

phi_x = 0
phi_y = 0
#phi_z = math.pi

dat_file = open("data_liss.txt" , "a+")



#time_step = 0.01

t = float(sys.argv[1])*0.003 #global time multiplied by scaling factor

#for t in range(time/time_step):
dat_file.write("%.16f\t%.16f\t\n"%( A_x*math.cos(w_x*t + phi_x) , A_y*math.sin(w_y*t + phi_y+math.pi/2)   ))
#t += time_step

dat_file.close()
