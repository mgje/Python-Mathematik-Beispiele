
#  Anzahl Primzahlen pro Intervall
# (c) Martin Guggisberg 2012

from matplotlib.pyplot import *
from math import *
import numpy as np


N = 10000000
be = 1000
gestrichen = [False]*(N+1)

for i in range(2,N+1):
    if not gestrichen[i]:
        for j in range(2*i,N+1,i):
            gestrichen[j] = True

gestrichen[0]=True
gestrichen[1]=True            

d=[]
for j in range(N/be):
    sum =0
    for k in range(j*be,(j+1)*be):
        if not gestrichen[k]:
            sum=sum+1
    d.append(sum)

#print d

x = np.linspace(0, N, N/be)
y = np.array(d)
plot(x,y)
show()
            
