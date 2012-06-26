# Polarkoordinatendarstellung
# (c) Martin Guggisberg 2012

from math import sqrt,pi
from cmath import phase
z1= -1+0j
z2= sqrt(2)/2*(1+1j)
z3= 2+2*sqrt(3)*1j

print "Die Komplexe Zahl %03f+%03fi hat den Betrag %g und den \
 Winkel %g Grad"%(z1.real,z1.imag,abs(z1),phase(z1)/pi*180)

print "Die Komplexe Zahl %03f+%03fi hat den Betrag %g und den \
 Winkel %g Grad"%(z2.real,z2.imag,abs(z2),phase(z2)/pi*180)

print "Die Komplexe Zahl %03f+%03fi hat den Betrag %g und den \
 Winkel %g Grad"%(z3.real,z3.imag,abs(z3),phase(z3)/pi*180)


