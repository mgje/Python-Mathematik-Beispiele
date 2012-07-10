import time
import math
from sympy import *

# Iterationsschritte Achtung Rekursion erlaubt max. 500
n = 800

# Stellen
stellen = 600

#Rekursive Methode (von links nach rechts)
def kbruch(x=1):
   if x == n:
      return n*n
   else:
      return N(x**2/((2*x+1)+kbruch(x+1)),stellen)

#Iterative Methode (von unten nach oben oder rechts nach links)
def kbruchitr():
   res = N(n**2,stellen)
   for i in range(n-1,0,-1):
      res = N(i**2/res+2*i-1,stellen)
   return res

   
time_begin = time.time()
pirek= N(4.0/(kbruch()+1),stellen)
time_end = time.time()
tot_time=time_end-time_begin
print "Fuer die rekursive Bestimmung von Pi auf %g Stellen braucht es %f Sekunden." %(stellen,tot_time)
print pirek


# Iterative Methode, von unten nach oben rechnen
time_begin = time.time()
piitr=kbruchitr()
time_end = time.time()
tot_time=time_end-time_begin

print '\n\nFuer die iterative Bestimmung von Pi auf %g Stellen braucht es %f Sekunden.'%(stellen,tot_time)
print N(4.0/piitr,stellen)
print '\n\nPi aus Python Bibliothek'
print N(pi,stellen)
print'\n\n'
n = 15000
stellen =10000
time_begin = time.time()
piitr=kbruchitr()
time_end = time.time()
tot_time=time_end-time_begin
print '\n\nFuer die iterative Bestimmung von Pi auf %g Stellen braucht es %f Sekunden.'%(stellen,tot_time)
print N(4.0/piitr,stellen)
print '\n\nPi aus Python Bibliothek'
print N(pi,stellen)
