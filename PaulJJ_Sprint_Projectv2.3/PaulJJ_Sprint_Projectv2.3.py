import sys
from time import sleep
from pylab import plot, show

words = "This is a test ;0;"
for char in words:
    sleep(0.5)
    sys.stdout.write(char)

x_num = [1, 2, 3]
y_num = [2, 4, 6]
plot (x_num, y_num)
show ()
##git pull --rebase
## hi
import matplotlib.pyplot as plt
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8,
55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years = range(2000, 2013)
plt.plot(years, nyc_temp, marker='o')
plt.title("Average Annual Temperature in NYC (2000-2012)")
plt.xlabel("Year")
plt.ylabel("Temperature (°F)")
plt.grid(True)
plt.show()
