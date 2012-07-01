
#  Anzahl Primzahlen pro Intervall
# (c) Martin Guggisberg 2012

from matplotlib.pyplot import *
from math import *
import numpy as np

N = 100000000  # Obere Grenze
be = 100000     # Intervall / Bereich
gestrichen = [False]*(N+1)

# Sieb des Eratosthenes
for i in range(2,N+1):
    if not gestrichen[i]:
        for j in range(2*i,N+1,i):
            gestrichen[j] = True

gestrichen[0]=True
gestrichen[1]=True            

# Liste Anzahl Primzahlen pro Intervall
d=[]

# Zu jedem Intervall
for j in range(N/be):
    sum =0
    # Summe der Primzahlen in diesem Intervall
    for k in range(j*be,(j+1)*be):
        if not gestrichen[k]:
            sum=sum+1
    d.append(sum)

# x-Skala gleichmaessig von 0 bis N
x = np.linspace(0, N, N/be)
y = np.array(d)
plot(x,y)
show()
            
