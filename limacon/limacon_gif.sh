#!/bin/bash

chmod +x limacon.py

for i in {1..160}
do
    python limacon.py $i
    gnuplot <<- EOF
        set object rectangle from screen 0,0 to screen 1,1 behind fillcolor rgb 'white' fillstyle solid noborder
        set polar
        unset tics
        unset raxis
        unset key
        set terminal png size 1024,1024
        set output "limacon_test_$i.png"
        plot 'limacon_dat.txt' with lines linetype 22
EOF
done


