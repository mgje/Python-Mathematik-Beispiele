#  Gift_Wachstum_optimistisch
#  (c) 2012 Martin Guggisberg 
import matplotlib.pyplot as pp

k=1.15
g=0.0
m=0.95
def f(x,y):
   return (k-g*y)*x

# x_n+1 = (k-g*y_n)*x_n
# y_n+1 = y_n+x_n

def genPopulation(x0,n):
   x=[x0]
   y=[0]
   # calculate 1..n-1 values
   for i in range(1,n):
      tmp = f(x[i-1],y[i-1])
      x.append(tmp)
      tmp2 = m*y[i-1]+x[i-1]
      y.append(tmp2)
   return x,y

x0 = 1.0
g=0.0001
popul,gift=genPopulation(x0,400)
pp.title("Wachstum mit Gift")
pp.plot(range(len(popul)),popul)
pp.show()
pp.title("Gift")
pp.plot(range(len(gift)),gift)
pp.show()
pp.title("Phasendiagramm")
g=0.0002
popul2,gift2=genPopulation(x0,400)
pp.plot(popul,gift,popul2,gift2)
pp.show()
