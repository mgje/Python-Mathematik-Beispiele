# Die glockenfoermige Gauss-Kurve
# (c) Martin Guggisberg 2012
# Wolfram Test:
# y=1/sqrt(2*pi*s)*exp((-1/2)((x-m)/s)^2),x=1.0,m=0,s=2.0

from math import sqrt,exp,pi

x=1.0
m=0.0
s=2.0

y = 1.0/(sqrt(2*pi*s))*exp((-1.0/2)*((x-m)/s)**2) 

print y
