
# ln(1+x)
# (c) Martin Guggisberg 2012

def L(x, n):
    s=0.0
    for i in range(1, n+1):
        s += (1.0/i)*((x/(1.0+x))**i)
    return s


def L2(x, n):
    a=x/(1.0+x)
    term = a
    s=a
    for i in range(2, n+1):
        term = a*term*(i-1)/i
        s += term
    return s



print L(0.2,1000)

print L2(0.2,1000)
