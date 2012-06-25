
# Flaecheninhalt eines Dreiecks
# (c) Martin Guggisberg 2012


# V = [[x1,y1],[x2,y2],[x3,y3]]
# x1 = V[0][0]
# y1 = V[0][1]
# x2 = V[0][0]

def A(V):
    z = V[1][0]*V[2][1]-V[2][0]*V[1][1]-V[0][0]*V[2][1]
    z = z + V[2][0]*V[0][1] + V[0][0]*V[1][1] - V[1][0]*V[0][1] 
    return 0.5*abs(z) 

print A([[0,0],[-1,0],[0,2]])

