#  Gift_Wachstum_optimistisch
#  (c) 2012 Martin Guggisberg 
import matplotlib.pyplot as pp

k,m,g=1.15,0.95,0.0001
x0 = 1.0

def f(x,y):
   return (k-g*y)*x

# x_n+1 = (k-g*y_n)*x_n
# y_n+1 = y_n+x_n

def genPopulation(x0,n):
   x,y=[x0],[0]
   # calculate 1..n-1 values
   for i in range(1,n):
      tmp = f(x[i-1],y[i-1])
      x.append(tmp)
      tmp2 = m*y[i-1]+x[i-1]
      y.append(tmp2)
   return x,y

popul,gift=genPopulation(x0,400)
pp.title("Wachstum mit Gift")
pp.plot(range(len(popul)),popul)
#pp.savefig('wachstum_gift.pdf')
pp.show()
pp.title("Gift")
pp.plot(range(len(gift)),gift)
#pp.savefig('gift.pdf')
pp.show()
pp.title("Phasendiagramm")
g=0.0002
popul2,gift2=genPopulation(x0,400)
pp.plot(popul,gift,popul2,gift2)
#pp.savefig('phasendiagramm.pdf')
pp.show()
