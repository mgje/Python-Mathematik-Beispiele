#  Exponenitelles_Wachstum
#  (c) 2012 Martin Guggisberg 
import matplotlib.pyplot as pp

w=0.02
def f(x):
   return (1.0+w)*x

# x_n+1 = (1+w)*x_n
def genPopulation(x0,n):
   x=[x0]
   # calculate 1..n-1 values
   for i in range(1,n):
      tmp = f(x[i-1])
      x.append(tmp)
   return x

x0 = 1.3
popul=genPopulation(x0,200)
pp.title("Exp Wachstum")
pp.plot(range(len(popul)),popul)
pp.show()
