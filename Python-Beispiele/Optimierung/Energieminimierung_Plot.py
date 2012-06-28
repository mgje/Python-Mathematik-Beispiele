#  Energieminimierung
#  2D coordinates of Mesh are stored in a 1-dim vector

import scipy.optimize as optimize
from math import sqrt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as pp

# Aufhaenge Punkte P1,P2
P1=[0.0,5.0]
P2=[4.0,8.0]
L=7

def potEnergie(X):
   e=X[1]+(L-sqrt((P1[0]-X[0])**2+(P1[1]-X[1])**2) \
           -sqrt((P2[0]-X[0])**2+(P2[1]-X[1])**2))**2*10
   return e

def drawfig(X):
   fig = pp.figure(1,figsize=(6,8))
   ax = fig.add_subplot(111, autoscale_on=False, xlim=(-0.1,4.4), ylim=(3.0,9.0))
   ax.xaxis.set_minor_locator(MultipleLocator(0.1))
   ax.yaxis.set_minor_locator(MultipleLocator(0.1))
   x_=[P1[0],X[0],P2[0]]
   y_=[P1[1],X[1],P2[1]]
   pp.plot(x_,y_,'bo', color='k', markersize=10)
   pp.plot(x_,y_,linewidth=2, color='b')
   pp.show()


x0=[2.0,7.5]
xopt = optimize.fmin(potEnergie,x0, xtol=1e-9, disp=True)
print(xopt)
drawfig(x0)
drawfig(xopt)





