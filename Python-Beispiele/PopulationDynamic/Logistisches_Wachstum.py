#  Logistisches_Wachstum
#  (c) 2012 Martin Guggisberg 
import matplotlib.pyplot as pp

w=0.0032
G=10.0
def f(x):
   return x+w*x*(G-x)

# x_n+1 = x_n+w*x_n*(G-x_n)
def genPopulation(x0,n):
   x=[x0]
   # calculate 1..n-1 values
   for i in range(1,n):
      tmp = f(x[i-1])
      x.append(tmp)
   return x

x0 = 1.0
popul=genPopulation(x0,300)
pp.title("Log Wachstum")
pp.plot(range(len(popul)),popul)
pp.show()
