#  Energieminimierung
#  2D coordinates of Mesh are stored in a 1-dim vector

import scipy.optimize as optimize
from math import sqrt

# Aufhaenge Punkte P1,P2
P1=[0.0,5.0]
P2=[4.0,8.0]
L=7

def potEnergie(X):
   e=X[1]+(L-sqrt((P1[0]-X[0])**2+(P1[1]-X[1])**2) \
           -sqrt((P2[0]-X[0])**2+(P2[1]-X[1])**2))**2*1000
   return e

x0=[2.0,4.5]
xopt = optimize.fmin(potEnergie,x0, xtol=1e-9, disp=True)
print(xopt)



