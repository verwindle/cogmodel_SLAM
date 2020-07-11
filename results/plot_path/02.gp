set term postscript eps enhanced color
set output "02.eps"
set size ratio -1
set xrange [-28.083370:19.086494]
set yrange [-4.126595:43.043270]
set xlabel "x [m]"
set ylabel "z [m]"
plot "02.txt" using 1:3 lc rgb "#FF0000" title 'Ground Truth' w lines,"02.txt" using 4:6 lc rgb "#0000FF" title 'Visual Odometry' w lines,"< head -1 02.txt" using 1:3 lc rgb "#000000" pt 4 ps 1 lw 2 title 'Sequence Start' w points
