
# Pfadlaenge 
# (c) Martin Guggisberg 2012


from math import sqrt

def pfadlaenge(P):
    L = 0.0
    for i in range(1,len(P)):
        L=L+sqrt((P[i][0]-P[i-1][0])**2+(P[i][1]-P[i-1][1])**2)
    return L    
    

print pfadlaenge([[0,0], [1,0],[1,2], [0,2]])

