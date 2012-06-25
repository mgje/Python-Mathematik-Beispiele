
# Gauss
# (c) Martin Guggisberg 2012

from math import pi,exp,sqrt

def gauss(x,m=0.0,s=1.0):
    return 1.0/sqrt(2.0*pi)/s*exp(-0.5*((x-m)/s)**2)

xl =[]    
x =-5.0
while (x <= 5):
    xl.append(x)
    x = x + 0.1 

print x

for i in xl:
    print gauss(i)



