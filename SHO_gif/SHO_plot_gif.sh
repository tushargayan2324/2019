#!/bin/bash

chmod +x SHO_plot.py

>data_SHO.txt

for i in {1..300}
do
    python SHO_plot.py $i
    gnuplot <<- EOF
        set terminal png size 512,512
        unset tics
        unset key
        unset border
        set arrow 1 from -2,-4,-6 to 2,-4,-6 ls 8 lw 2
        set arrow 2 from -2,-4,-6 to -2,4,-6 ls 22 lw 2
        set arrow 3 from -2,-4,-6 to -2,-4,6 ls 7 lw 2
        set label 1 'x' at 2,-4,-6 tc 'black'
        set label 2 'y' at -2,4,-6 tc 'blue'
        set label 3 'z' at -2,-4,6 tc 'red'
        
        set style line 2 lc rgb 'black' pt 7
        set view 60 + $i*0.5 , 0 + $i
        set output "SHO_gif_$i.png"
        splot [-2:2][-4:4][-6:6] 'data_SHO.txt' with lines lt 22 lw 2
EOF
done
