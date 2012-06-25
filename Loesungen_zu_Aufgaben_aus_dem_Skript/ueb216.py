
# sin(x) approximieren 
# (c) Martin Guggisberg 2012

from math import sin,pi

x = pi/6

Ntot = 13
zahl=1.0

for k in range(1,Ntot+1):
    zahl=zahl*(1-x**2/(k**2*pi**2))
    
zahl=x*zahl

print 'sin(%g) approximiert mit %d Glieder ist %g'%(x/pi*180,Ntot,zahl)
print 'sin(%g) =  %g' % (x/pi*180,sin(x))

