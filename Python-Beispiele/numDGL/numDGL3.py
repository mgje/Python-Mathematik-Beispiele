# -*- coding: utf-8 -*-


import numpy as np
from scipy.integrate import odeint # Abkürzung
import pylab as pl

from ipHelp import IPS, ip_syshook


# rein numerisch:

N = 1000
xx = np.linspace(-1.0,1.0,N)

dx = xx[1]-xx[0]

yy = xx * np.sin(xx)

# Differenzenquotient
yy_d = np.diff(yy) / dx # ! Ergebnis hat länge N-1

# Numerische Integration (Rechteckflächen summieren)
yy_i = np.cumsum(yy) * dx 


pl.plot(xx, yy, label='y(x)')
pl.plot(xx[:-1], yy_d, label='Ableitung')
pl.plot(xx, yy_i, label='Stammfunktion')




# symbolisch

import sympy as sp

x = sp.Symbol('x')
y = x*sp.sin(x)

y_d = y.diff(x)
y_i = y.integrate(x)

y_fnc = sp.lambdify(x, y, modules='numpy')
y_d_fnc = sp.lambdify(x, y_d, modules='numpy')
y_i_fnc = sp.lambdify(x, y_i, modules='numpy')


xx2 = np.linspace(xx[0], xx[-1],N/50)
pl.plot(xx2, y_fnc(xx2), 'bo', label=str(y))
pl.plot(xx2, y_d_fnc(xx2), 'go', label=str(y_d))
pl.plot(xx2, y_i_fnc(xx2), 'ro', label=str(y_i))


# dünne Linien mit höherer Auflösung
pl.plot(xx, y_fnc(xx), 'b:', label=None)
pl.plot(xx, y_d_fnc(xx), 'g:', label=None)
pl.plot(xx, y_i_fnc(xx), 'r:', label=None)


pl.legend(loc=4)

#IPS()


# Wenn man reinzoomt sieht man die Unterschiede zwischen
# numerischer und symbolischer (exakter) Rechnung

# Stammfunktion unterscheidet sich um eine Konstante (nicht weiter überaschend)


pl.show()
