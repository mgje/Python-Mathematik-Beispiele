# -*- coding: utf-8 -*-


"""
Beispielskript zum Thema
 * numerische Lösung gewöhnlicher DGLn
"""

import numpy as np
from scipy.integrate import odeint # Abkürzung
import pylab



delta=0.1   # delta:= 1/2*d/m         
omega_2=100 # omega_2:=c/m (_2 symbolisiert hier 'quadrat')


t=np.arange(0,100,.01) # unabhängige Variable (Zeit)


x0=[10,0]   # Anfangszustand für x, und x_dot



def rhs(x,t):
    """
    rhs = "right hand side [function]"

    Diese Funktion gibt die erste Zeitableitung des Zustandsvektors x
    abhängig vom aktuellen Zustand x und der Zeit t zurück
    """
    x1_dot=x[1]
    x2_dot=-(2*delta*x[1]+omega_2*x[0])
    
    return [x1_dot, x2_dot]
    

x=odeint(rhs, x0, t,)

# x ist jetzt ein 1000-zeiliges zweispaltiges Datenfeld
# erste Spalte x1, zweite x2


x1=x[:,0]
x2=x[:,1]


# alternativ:
# x1, x2 = list(x.T)


pylab.plot(t, x1, "k-")
pylab.show()
