from math import *

def distanz(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    

def schwerpunkt(punkte):
    x0=y0=0.0
    n = len(punkte)
    for P in punkte:
        x0=x0+P[0]
        y0=y0+P[1]
    return (x0/n,y0/n)



def WeiszmanIteration(P, punkte):
    """
    Return a new approximation to the geometric median 
    of `points` by applying one iteration of Weiszfeld's 
    algorithm to the old appromixation P.
    """
    W = x = y = 0.0
    for Q in punkte:
        d = distanz(P, Q)
        if d != 0:
            w = 1.0 / d
            W += w
            x += Q[0] * w
            y += Q[1] * w
    return x / W, y / W


def fermatpunkt(punkte, epsilon):
    """
    Return an approximation to the geometric median for 
    `points`. Start with the centroid and apply Weiszfeld's 
    algorithm until the distance between steps is less 
    than `epsilon`.
    """
    P = schwerpunkt(punkte)
    while True:
        Q = WeiszmanIteration(P, punkte)
        if distanz(P, Q) < epsilon:
            return Q
        P = Q
        
# Initialisierung der Punkte A-F        
Punkte = []
A = [3,10]
Punkte.append(A)    
B = [4,9]
Punkte.append(B) 
C = [6,10]
Punkte.append(C) 
D = [6,6]
Punkte.append(D) 
E = [10,7]
Punkte.append(E) 
F = [4,7]
Punkte.append(F) 

print Punkte
print schwerpunkt(Punkte)    
print distanz(C,D)   
print WeiszmanIteration(F,Punkte)   
print fermatpunkt(Punkte, 0.01)  
            
            