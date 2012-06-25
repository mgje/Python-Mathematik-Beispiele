
# Umrechnung Polar in Kartesische Koordinaten
# (c) Martin Guggisberg 2012

from cmath import e, pi

z1= 2*e**(1j*pi/6)
z2= 2*e**(1j*2*pi/3)
z3= 2*e**(1j*pi/4)

print "Komplexe Zahl: %03f+%03fi"%(z1.real,z1.imag)

print "Komplexe Zahl: %03f+%03fi"%(z2.real,z2.imag)

print "Komplexe Zahl: %03f+%03fi"%(z3.real,z3.imag)
