
# numerische Integration
# (c) Martin Guggisberg 2012
# Test Wolfram Alpha
# int (exp(x)) for  0 to ln(3)
# int (cos(x)) for  0 to pi
# int (sin(x)) for  0 to pi/2

from math import pi,exp,sqrt,sin,cos,tan,log

def integral1(f,a,b):
    return (b-a)*(f(a)+f(b))/2.0


def integral2(f,a,b,n=100):
    sum =0.0
    step =(float(b)-float(a))/n
    for i in range (n):
      sum = sum + integral1(f,i*step,(i+1)*step)
    return sum  


def f1(x):
    return exp(x)

def f2(x):
    return cos(x)

def f3(x):
    return sin(x)


print "Integral1 ist %g" % integral2(f1,0,log(3))
print "Integral1 ist %g" % integral2(f2,0,pi)
print "Integral1 ist %g" % integral2(f3,0,pi/2)

