
# Sieb des Eratosthenes
# (c) Martin Guggisberg 2012

N = 10000000
gestrichen = [False]*(N+1)

for i in range(2,N+1):
    if not gestrichen[i]:
        print i
        for j in range(2*i,N+1,i):
            gestrichen[j] = True
            
