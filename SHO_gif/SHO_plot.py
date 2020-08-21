
import math,sys

A_x = 2
A_y = 4
A_z = 6

w_x = 1
w_y = 2
w_z = math.pi

phi_x = 0
phi_y = (math.pi)/2
phi_z = math.pi

dat_file = open("data_SHO.txt" , "a+")

#time_step = 0.01

#time = 0 #(seconds/ global time)
t = float(sys.argv[1])*0.1 #global time

#for t in range(time/time_step):
    #dat_file.write( A_x*math.cos(w_x*t + phi_x) , A_y*math.cos(w_y*t + phi_y) , A_z*math.cos(w_z + phi_z) % % % )
dat_file.write("%.16f\t%.16f\t%f\n"%( A_x*math.cos(w_x*t + phi_x) , A_y*math.cos(w_y*t + phi_y) , A_z*math.cos(w_z*t + phi_z) ))
#t += time_step

dat_file.close()
