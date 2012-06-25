
# Funktionstabelle erstellen
# (c) Martin Guggisberg 2012

# v(t) = v0*t + 0.5 * g * t**2

from math import *

g=9.81
v0 = 1.0
N = 11

t_0 = 0.0
t_e = 2.0*v0/g
t_i = (t_e-t_0)/N

print 't        y(t) '
t = t_0
while (t <= t_e):
    y = v0*t + 0.5 * g * t**2
    print '%5.3f    %5.3f' % (t, y)
    t = t + t_i




