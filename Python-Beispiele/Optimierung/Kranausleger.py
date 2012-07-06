#  Kranausleger
#  2D coordinates of Mesh are stored in a 1-dim vector
#  X =[x0,y0,x1,y1,...]
# (c) Martin Guggisberg 2012
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import scipy.optimize as optimize
from math import sqrt
import matplotlib.pyplot as pp
# Geometrie des Problems / Knoten 0 und 1 werden fixiert.
# 1  6  5
#
# 0  2  3  4  
# Gewicht haengt an Knoten 4 der y-Wert steht an der Stelle 7   

def feder(i,j,K,L,X):
   """Input Knoten i,j ; Federkonstante K ; Laenge L
        Rueckgabe Energie in der Feder"""
   xi = 2*i
   xj = 2*j 
   return 0.5*K*(L-sqrt((X[xi]-X[xj])**2+(X[xi+1]-X[xj+1])**2))**2
                      
def gesEnergie(x,x_fix,m):
   """Alle Verstrebungen des Kranauslegers und das Gewicht am Ende 
   tragen zur Gesamtenergie bei """
   #Gitterpunkte als Vektor x,y, ...
   X=x_fix[:]
   for el in x:
           X.append(el)
   
   # Geometrie
   #Horizontal unten
   e=feder(0,2,100.0,1.0,X)
   e+=feder(2,3,100.0,1.0,X)
   e+=feder(3,4,100.0,1.0,X)
   #Horizontal oben
   e+=feder(1,6,100.0,1.0,X)
   e+=feder(6,5,100.0,1.0,X)
   #Vertikal
   e+=feder(6,2,100.0,1.0,X)
   e+=feder(5,3,100.0,1.0,X)
   #Schraeg
   e+=feder(1,2,100.0,1.414,X)
   e+=feder(6,3,100.0,1.414,X)
   e+=feder(5,4,100.0,1.414,X)
   e+=9.81*m*X[9]
   return e

def plotGelenk(i,j,x):
    print [x[i*2],x[j*2]]
    pp.plot([x[i*2],x[j*2]],[x[i*2+1],x[j*2+1]],linewidth=2, color='b')

def plotKnoten(X):
   #Knoten x_ y_
   x_=[]
   y_=[]
   for i in range(0,len(X),2):
      x_.append(X[i])
      y_.append(X[i+1])

   pp.plot(x_,y_,'bo', color='k', markersize=10)
    
def plotAusleger(X):
   fig = pp.figure(2,figsize=(8,3))
   ax = fig.add_subplot(111, autoscale_on=False, xlim=(-0.05,3.05), ylim=(-0.6,1.00))
   ax.xaxis.set_minor_locator(MultipleLocator(0.1))
   ax.yaxis.set_minor_locator(MultipleLocator(0.1))
   plotGelenk(0,2,X)
   plotGelenk(2,3,X)
   plotGelenk(3,4,X)
   plotGelenk(1,6,X)
   plotGelenk(6,5,X)
   plotGelenk(6,2,X)
   plotGelenk(5,3,X)
   plotGelenk(1,2,X)
   plotGelenk(6,3,X)
   plotGelenk(5,4,X)
   plotKnoten(X)



# Fixierte Knoten 0,1
x_fix=[0.0,0.0,0.0,1.0]

#  Variable Knoten 2,3,4,5,6
x0=[1.0,0.0,2.0,0.0,3.0,0.0,2.0,1.0,1.0,1.0]

# Vernuenftige Massen liegen im Bereich 0.001 bis 0.2
m=0.2
xopt = optimize.fmin(gesEnergie,x0,args=(x_fix,m), xtol=1e-6, disp=True)
print(xopt)

# Plot Kranausleger ohne Last 

X=x_fix[:]
for el in x0:
    X.append(el)

plotAusleger(X)
pp.show()

# Plot Kranausleger mit Last 
X=x_fix[:]
for el in xopt:
    X.append(el)

plotAusleger(X)

pp.show()





