# Zahlenmauer 
# (c) Martin Guggisberg 2016

l=[4,2,8,9,1,3,4]

while len(l)>0:
    print l
    n = len(l)
    n_l = []
    for i in range(n-1):
        n_l.append(l[i]+l[i+1])
    l = n_l
        