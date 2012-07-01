# Pi approximieren mit Kettenbruch
# (c) Martin Guggisberg 2012

from math import pi

N = 9

# Von unten nach oben rechnen
res = float(N**2)
for n in range(N-1,0,-1):
   res = n**2/res+2*n-1

print 'Pi approximiert mit %d Gliedern ist %1.6f'%(N,4/res)
print 'Pi aus Math Bibliothek ist %1.6f' % pi
