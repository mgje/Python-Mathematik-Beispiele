# Ei kochen
# (c) Martin Guggisberg 2012

from math import log,sqrt,exp,pi

M=67.0
rho=1.038
capa=3.7
K=5.4E-3

TW=100.0
T0=4.0
Ty=70


t = (M**(2.0/3.0)*capa*rho**(1.0/3.0))/(K*pi**2*(4*pi/3.0)**(2.0/3.0))\
    *log(0.76*(T0-TW)/(Ty-TW))

print t/60
