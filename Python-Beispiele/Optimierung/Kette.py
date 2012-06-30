#  Kette
#  (c) 2012 Martin Guggisberg

import scipy.optimize as optimize
from math import sqrt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as pp
import random

# Aufhaenge Punkte P1,P2
P1=[0.0,0.0]
P2=[10.0,0.0]
#Anzahl Glieder
N=17
#Laenge der Kette
L=12.0

#Laenge eines Glieds
lg = L/N

# Paramtrisierung
# Fuer N=5 Glieder
# F-x0-x1-x2-x3-F
# 4 (N-1) freie Koordinaten 

def potEnergie(X):
   w = []
   w.append(P1[0])
   w.append(P1[1])
   for el in X:
      w.append(el)
   w.append(P2[0])
   w.append(P2[1])
   #print w
   sum=0.0
   for i in range(N):
      x=2*i
      y=2*i+1
      ll =sqrt((w[x]-w[x+2])**2+(w[y]-w[y+2])**2)
      sum+=ll*(w[y]+w[y+2])/2.0+70*(lg-ll)**2
      #print lg,ll

   return sum

def drawfig(X):
   fig = pp.figure(1,figsize=(10,5))
   ax = fig.add_subplot(111, autoscale_on=False, xlim=(-0.1,10.1), ylim=(-5.0,0.1))
   ax.xaxis.set_minor_locator(MultipleLocator(0.1))
   ax.yaxis.set_minor_locator(MultipleLocator(0.1))
   x_=[P1[0]]
   y_=[P1[1]]
   for i in range(N-1):
      x=2*i
      y=2*i+1
      x_.append(X[x])
      y_.append(X[y])

   x_.append(P2[0])
   y_.append(P2[1])   
   
   pp.plot(x_,y_,'bo', color='k', markersize=10)
   pp.plot(x_,y_,linewidth=2, color='b')
   pp.show()

#Generate Initial Vektor
x0=[]
d = 10.0/N
pos =d
print N
for i in range(N-1):
   x0.append(pos)
   x0.append((pos-5)**2/7-3.4)
   pos +=d

print(x0)

xopt = optimize.fmin(potEnergie,x0, xtol=1e-10, disp=True,maxiter=100000000, maxfun=9000000)
print(xopt)
drawfig(x0)
drawfig(xopt)





