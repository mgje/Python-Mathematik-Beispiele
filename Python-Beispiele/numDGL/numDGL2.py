# -*- coding: utf-8 -*-


import numpy as np
from scipy.integrate import odeint # Abkürzung
import pylab

from ipHelp import IPS, ip_syshook




def rhs(x,t):
    """
    rhs = "right hand side [function]"

    Diese Funktion gibt die erste Zeitableitung des Zustandsvektors x
    abhängig vom aktuellen Zustand x und der Zeit t zurück
    """

    # DGL 2. Ordnung -> System von 2 DGLn 1. Ordnung
    # x1 := x
    # x2 := x_dot
    # daraus folgt:
    # x1_dot = x2
    # x2_dot = <gegebene Formel nach x_ddot umgestellt> 


    # a ist nicht lokal definiert
    # -> es wird im nächst höheren Namensraum danach gesucht

    x1_dot=x[1]
    x2_dot=- (x[1] + x[0]**3 + a*x[0])
    
    return [x1_dot, x2_dot]


a_werte = [-1, 0, 1]
t = np.linspace(0, 55, 2000)
x0 = [5, 0]


for a in a_werte:
    #IPS()

    #import sys
    #sys.exit()

    x=odeint(rhs, x0, t,)
    x1, x2 = list(x.T)
    pylab.plot(t, x1, label='a=%i' %a)

pylab.legend()
pylab.show()
