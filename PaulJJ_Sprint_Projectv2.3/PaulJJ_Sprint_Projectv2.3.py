import sys
from time import sleep
from pylab import plot, show

words = "This is just a test :P"
for char in words:
    sleep(0.5)
        sys.stdout.write(char)

x_num = [1, 2, 3]
y_num = [2, 4, 6]
plot (x_num, y_num)
show ()