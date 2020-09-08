#!/bin/bash

chmod +x lissagious.py

>data_liss.txt

for i in {1..600}
do
    python lissagious.py $i
    gnuplot <<- EOF
        unset tics;unset key;unset border
        set arrow 1 from cos(0.012*$i ),sin(0.012*$i)+3 to cos(0.012*$i ),sin(0.024*$i+pi/2) nohead ls 8 lw 2
        set arrow 2 from cos(0.024*$i+pi/2)-3,sin(0.024*$i+pi/2) to cos(0.012*$i ),sin(0.024*$i+pi/2) nohead ls 8 lw 2
        
        set parametric
        plot cos(t)-3,sin(t) lt 22 lw 2
        replot cos(t),sin(t)+3 lt 22 lw 2
        replot 'data_liss.txt' with lines lt 22 lw 2
        
        set xrange [-5:5]
        set yrange [-5:5]
        set terminal png size 512,512
        set output "liss_gif_$i.png"
        replot
EOF

done

