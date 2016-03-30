# Zahlenmauer 2
# (c) Martin Guggisberg 2016
import itertools

def calc_zahlenmauer(l):
    while len(l)>1:
        n = len(l)
        n_l = []
        for i in range(n-1):
            n_l.append(l[i]+l[i+1])
        l = n_l
    return l[0]
        

l=[2,3,4,5,6,7,8,9]
print calc_zahlenmauer(l)

mx = 0
for l in list(itertools.permutations(l)):
    tmp=calc_zahlenmauer(l)
    if tmp > mx:
        mx = tmp
    print tmp

print "die grösste Mauer liefert die Summe:",mx