
# Pi approximieren mit Kettenbruch
# (c) Martin Guggisberg 2012

from math import pi

Ntot = 3
z=[]
n=[1]
ug=1

for i in range(1,Ntot+1):
    z.append(i**2)
    ug = ug+2
    n.append(ug)
     
print z
print n

# von unten nach oben rechenen
zahl = float(n[-1])
ni =-1

for i in range(Ntot):
    print zahl
    print n[ni-1]
    zahl = z[ni]/zahl+n[ni-1]
    ni = ni -1
    

print 'Pi approximiert mit %d Summanden ist %g'%(Ntot,4/zahl)
print 'Pi aus Math Bibliothek ist %g' % pi

