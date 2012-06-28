#  numOptimierung
# (c) Martin Guggisberg 2012
from scipy import optimize

def f(x):
   return x[0]**2 + (x[1]-2)**2

print optimize.fmin(f, [0,0])
