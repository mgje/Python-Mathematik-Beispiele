# -*- coding: utf-8 -*-

"""
Beispielskript zu den Themen
 * Regression und Interpolation
 * splines
"""


import numpy as np
import scipy as sc
import pylab as pl


# Quelle: http://www.scipy.org/Cookbook/LinearRegression
# angepasst


#####################################################

#Regression

#####################################################




#Linear regression example
# This is a very simple example of using two scipy tools 
# for linear regression, polyfit and stats.linregress

#Sample data creation
#number of points 
n=10
t=np.linspace(-5,5,n)
#parameters
a=0.02; b=0.8; c=-1
x=sc.polyval([a,b,c],t) # alternativ: x = a*t+b
#add some noise
x_noise=x+0.4*sc.randn(n)

#Linear regressison -polyfit - polyfit can be used other orders polys
(ar,br)=sc.polyfit(t,x_noise,1)
xr=sc.polyval([ar,br],t)

# Quadratische Regression:
q2, q1, q0 = sc.polyfit(t,x_noise,2)
xqr=sc.polyval([q2,q1,q0],t)


# Bildgröße wird in Zoll erwartet -> Umrechnungsfaktor
mm = 1./25.4 #mm to inch
fs = [90*mm, 60*mm]
pl.figure(figsize=fs)# benutzerdef. Bildgröße erzwingen

pl.plot(t, x_noise, 'ro') # Daten
pl.savefig('bsp3_1.pdf')
pl.plot(t, xr, lw=2) # lw = linewidth
pl.savefig('bsp3_2.pdf')
pl.plot(t, xqr, 'g--', lw=2)
pl.savefig('bsp3_3.pdf')


#####################################################

#Interpolation

#####################################################



#siehe auch: http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html

# normalerweise sollten alle imports an den Anfang,
# aber damit man sieht, dass man das erst hier braucht:


from scipy.interpolate import interp1d

func1 = interp1d(t, x_noise) # kind = 'linear' ist standard
func0 = interp1d(t, x_noise, kind='nearest') # Ordnung 0 ist 'nearest' (neighbor)
func3 = interp1d(t, x_noise, kind=3) # kubischer spline

t_highres = np.linspace(t[0],t[-1],100)

xi0 = func0(t_highres)
xi1 = func1(t_highres)
xi3 = func3(t_highres)

# plotten
#neues Bild
pl.figure(figsize=fs)# benutzerdef. Bildgröße erzwingen

pl.plot(t, x_noise, 'ro',) # Daten
pl.plot(t_highres, xi0, 'bo', ms = 2)
pl.plot(t_highres, xi1, 'g', lw = 1.3)
pl.savefig('bsp3_4.pdf')
pl.plot(t_highres, xi3, 'k-', lw = 2)
pl.savefig('bsp3_5.pdf')


#####################################################

# "Smoothing Spline"
#http://www.scipy.org/Cookbook/Interpolation

#####################################################




from scipy.interpolate import splrep, splev
# spline parameters
s=0.4 # smoothness parameter
k=2 # spline order
nest=-1 # estimate of number of knots needed (-1 = maximal)

tck = splrep(t, x_noise,s=s,k=k)

tck2 = splrep(t, x_noise,s=0.0,k=k)

# evaluate spline, including interpolated points
t_highres = np.linspace(t[0],t[-1],100)
xspline = splev(t_highres,tck)

xspline2 = splev(t_highres,tck2)



#neues Bild
pl.figure(figsize=fs)# benutzerdef. Bildgröße erzwingen

pl.plot(t, x_noise, 'ro') # Daten
pl.plot(t_highres, xspline, lw = 1.5)
pl.savefig('bsp3_6.pdf')
pl.plot(t_highres, xspline2, 'g--', lw = 2)
pl.savefig('bsp3_7.pdf')

pl.show()