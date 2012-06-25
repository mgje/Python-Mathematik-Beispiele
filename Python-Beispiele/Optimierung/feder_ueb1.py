import scipy.optimize as optimize
from math import sqrt
# Knoten Kran
#x=[0.0,1.0,2.0,3.0,2.0,1.0,0.0]
#y=[0.0,0.0,0.0,0.0,1.0,1.0,1.0]

def feder(i,j,K,L,X):
   """Input Knoten i,j ; Federkonstante K ; Laenge L
        Rueckgabe Energie in der Feder"""
   xi = 2*i
   xj = 2*j 
   return 0.5*K*(L-sqrt((X[xi]-X[xj])**2+(X[xi+1]-X[xj+1])**2))**2
                      
def gesEnergie(x,x_fix,m):
   #Gitterpunkte als Vektor x,y, ...
   X=x_fix[:]
   for el in x:
           X.append(el)
   
   print X
   print len(X)
   e=feder(0,1,100.0,1.0,X)
   e+=9.81*m*X[3]
   return e

x0=[0.0,1.0]
x_fix=[0.0,0.0]
m=20
xopt = optimize.fmin(gesEnergie,x0,args=(x_fix,m), xtol=1e-2, disp=True)
print(xopt)
