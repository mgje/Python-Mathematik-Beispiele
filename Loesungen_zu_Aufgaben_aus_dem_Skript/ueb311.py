
# Geschwindigkekit und Beschleunigung
# (c) Martin Guggisberg 2012

from math import pi,exp,sqrt,sin,cos,tan,log  

def a(x,t,dt=1E-5):
    return (x(t+dt)-2*x(t)+x(t-dt))/(dt**2)

def v(x,t,dt=1E-5):
    return (x(t+dt)-x(t-dt))/(2*dt)

def x(t):
    return exp((t-4)**2)


def kinematics(x,t,dt=1E-4):
    print "Ort: %g"%x(t)
    print "Geschwindigkeit: %g"%v(x,t,dt)
    print "Beschleunigung: %g"%a(x,t,dt)


kinematics(x,5,1E-5)
