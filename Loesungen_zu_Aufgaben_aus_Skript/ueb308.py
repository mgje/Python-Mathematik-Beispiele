
# numerisch Ableiten
# (c) Martin Guggisberg 2012
# Test Wolframalpha
# diff( exp(x) ) for x=0
# diff( exp(-2x^2) ) for x=0
# diff( cos(x) ) for x=2pi



from math import pi,exp,sqrt,sin,cos,tan,log

def ableitung(x,f,h=0.001):
    return (f(x+h)-f(x-h))/(2*h)


def f0(x):
    return exp(x)

def f1(x):
    return exp(-2*x*x)

def f2(x):
    return cos(x)

def f3(x):
    return log(x)



print "Die Ableitung der Funktion exp(x) an der Stelle %g beträgt %g" % (0,ableitung(0,f0))
print "Die Ableitung der Funktion exp(-2x^2) an der Stelle %g beträgt %g" % (0,ableitung(0,f1))
print "Die Ableitung der Funktion cos(x) an der Stelle %g beträgt %g" % (2*pi,ableitung(2*pi,f2))
print "Die Ableitung der Funktion ln(x) an der Stelle %g beträgt %g" % (1,ableitung(1.0,f3))
