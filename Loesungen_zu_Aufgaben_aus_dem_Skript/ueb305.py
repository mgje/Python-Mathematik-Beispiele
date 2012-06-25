
# Approx Pi mit Pfad 
# (c) Martin Guggisberg 2012

from math import sqrt,pi,sin,cos

def pfadlaenge(P):
    L = 0.0
    for i in range(1,len(P)):
        L=L+sqrt((P[i][0]-P[i-1][0])**2+(P[i][1]-P[i-1][1])**2)
    return L    


k = 15
n = 2**k

punkte =[]
for i in range(n+1):
    x = 0.5*cos(2*pi*i/n)
    y = 0.5*sin(2*pi*i/n)
    punkte.append([x,y])
    

print pfadlaenge(punkte)
print pi

