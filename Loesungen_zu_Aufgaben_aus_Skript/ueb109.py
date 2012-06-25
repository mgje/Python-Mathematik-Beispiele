# Komplexe Zahlen / Terme berechen
# (c) Martin Guggisberg 2012

from math import sqrt

z1 = (2-1j)/(1+1j)
print z1
print z1.real
print z1.imag

zaehler = (sqrt(3)+(2*sqrt(2)*1j))
nenner = (sqrt(3)- (sqrt(2)*1j))
z2 = zaehler/nenner
print z2
print z2.real
print z2.imag

zaehler =(2+1j)*(3-2j)*(1+2j)
nenner = (1-1j)**2
z3 = zaehler/nenner
print z3
print z3.real
print z3.imag
