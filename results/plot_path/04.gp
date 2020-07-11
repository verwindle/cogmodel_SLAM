set term postscript eps enhanced color
set output "04.eps"
set size ratio -1
set xrange [-226.611420:218.867493]
set yrange [-20.249039:425.229858]
set xlabel "x [m]"
set ylabel "z [m]"
plot "04.txt" using 1:3 lc rgb "#FF0000" title 'Ground Truth' w lines,"04.txt" using 4:6 lc rgb "#0000FF" title 'Visual Odometry' w lines,"< head -1 04.txt" using 1:3 lc rgb "#000000" pt 4 ps 1 lw 2 title 'Sequence Start' w points
