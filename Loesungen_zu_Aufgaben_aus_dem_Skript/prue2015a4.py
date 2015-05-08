## Berechnung einer stückweise definierten Funktion

def welle(x):
    res = 0.0
    if 0.0<x<=2.0:
        res = 1-(x-1.0)**2
    if 2.0<x<=4.0:
        res = -1+(x-3.0)**2
    return res

print welle(1.0)
print welle(2.0)


from gpanel import *
makeGPanel(-1,5,-1.1,1.1)

x = -10.0
dx = 0.05
xmax = 10.0
move(x,welle(x))

while x < xmax:
    y = welle(x)
    draw(x,y)
    x = x +dx




