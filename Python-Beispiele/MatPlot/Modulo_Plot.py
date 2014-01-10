
#  Anzahl Primzahlen pro Intervall
# (c) Martin Guggisberg 2012

from matplotlib.pyplot import *
from math import *
import numpy as np

#Obere Grenze
N = 1000000

# Liste Anzahl Primzahlen pro Intervall
d = []
c = []

# Zu jedem Intervall
for j in range(1, N):
    c.append(j)
    d.append((2**j) % N)

# x-Skala gleichmaessig von 0 bis N
print d
x = np.array(c)
y = np.array(d)
plot(x, y, 'ro')
show()
