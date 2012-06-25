
# Reziproke quadratische Summe
# (c) Martin Guggisberg 2012

def s(M):
    sum = 0.0
    for k in range(1,M+1):
        sum = sum + 1.0/k**2
    return sum 


print s(3)
# Test
print 1+1.0/(2*2)+1.0/(3*3)
