
# Fourier
# (c) Martin Guggisberg 2012

from math import pi,sin

def f(t,T):
    if (t<T/2.0) and (t>0):
        return 1.0
    if (t>T/2.0) and (t<T):
        return -1.0
    return 0

def S(t,n,T):
    z = 0.0
    for i in range(1,n+1):
        z = z + 1.0/(2*i-1)*sin(2*(2*i-1)*pi*t/T)
    return 4/pi*z

# Test
T = pi
n = [1,3,5,10,30,100]
t = [0.0628,1.57,3.08]

print 'Berechnung f(t) '
print '     f(x)     '+'  '.join(['S(t,%3d,T)'% ni for ni in n])
  
for ti in t:
    out=[]
    out.append(f(ti,T))
    for ni in n:
        out.append(S(ti,ni,T))
    line= ' '.join(['%11.3f' % x for x in out])
    print line

print
print 'Fehler (S(t,N)-f(t))/f(t) '
print '     f(x)     '+'  '.join(['S(t,%3d,T)'% ni for ni in n])
  
for ti in t:
    out=[]
    out.append(f(ti,T))
    for ni in n:
        out.append(S(ti,ni,T))
    x0=out[0]    
    line= ' '.join(['%11.3f' % abs((x-x0)/x0) for x in out])
    print line


