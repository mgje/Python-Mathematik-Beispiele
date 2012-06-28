
#  Plot Lines
#  2D coordinates of Mesh are stored in a 1-dim vector
#  X =[x0,y0,x1,y1,...]
# (c) Martin Guggisberg 2012

import matplotlib.pyplot as pp

def plotGelenk(i,j,x):
    print [x[i*2],x[j*2]]
    pp.plot([x[i*2],x[j*2]],[x[i*2+1],x[j*2+1]],linewidth=2, color='b')


x0=[1.0,0.0,2.0,0.0,3.0,0.0,2.0,1.0,1.0,1.0]
x_fix=[0.0,0.0,0.0,1.0]
X=x_fix[:]
for el in x0:
    X.append(el)
   

pp.figure()

fig = pp.figure(1,figsize=(8,5))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1,5), ylim=(-2,4))
# 1  6  5
#
# 0  2  3  4 

plotGelenk(0,1,X)
plotGelenk(6,2,X)
plotGelenk(5,3,X)
plotGelenk(1,6,X)
plotGelenk(5,6,X)
plotGelenk(5,4,X)
plotGelenk(3,4,X)
plotGelenk(3,2,X)
plotGelenk(0,2,X)

#pp.plot([x[0],x[2]],[x[1],x[3]])

pp.show()
            
