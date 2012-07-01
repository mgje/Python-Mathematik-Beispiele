# Ei kochen
# (c) Martin Guggisberg 2012

from math import log,sqrt,exp,pi

M=67.0      # Masse  
rho=1.038   # Dichte
capa=3.7    # spez. Wörmekapazität
K=5.4E-3    # Termische Leitfaehigkeit

TW=100.0    # Temp kochendes Wasser
T0=4.0      # Anfangstemperatur
Ty=70       # Endtemperatur


t = (M**(2.0/3.0)*capa*rho**(1.0/3.0))/(K*pi**2*(4*pi/3.0)**(2.0/3.0))\
    *log(0.76*(T0-TW)/(Ty-TW))

print t/60
