
# numerische Integration
# (c) Martin Guggisberg 2012

from math import pi,exp,sqrt,sin,cos,tan,log

def integration(f,a,b):
    return (b-a)*(f(a)+f(b))/2.0


def f0(x):
    return exp(x)

print integration(f0,0,1)


def f1(x):
    return exp(-2*x*x)

def f2(x):
    return cos(x)

def f3(x):
    return log(x)


