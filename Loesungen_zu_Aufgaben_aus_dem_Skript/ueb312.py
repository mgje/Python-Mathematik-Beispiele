
# Kinematics 2
# Geschwindigkekit und Beschleunigung
# (c) Martin Guggisberg 2012

from math import pi,exp,sqrt,sin,cos,tan,log  
from numpy import *

def a(r,t,dt=1E-5):
    return (r(t+dt)-2*r(t)+r(t-dt))/(dt**2)

def v(r,t,dt=1E-5):
    return (r(t+dt)-r(t-dt))/(2*dt)


def r(t,R=1,w=2*pi):
    return array([R*cos(w*t),R*sin(w*t)])


def kinematics2(r,t,dt=1E-4):
    print "Ort: <%g,%g>"%(r(t)[0],r(t)[1])
    print "Geschwindigkeit: <%g,%g>"%(v(r,t,dt)[0],v(r,t,dt)[1])
    print "Beschleunigung: <%g,%g>"%(a(r,t,dt)[0],a(r,t,dt)[1])


kinematics2(r,1,1E-5)
