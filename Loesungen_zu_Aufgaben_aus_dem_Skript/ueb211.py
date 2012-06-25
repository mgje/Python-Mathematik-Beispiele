
# Verschachtelte Liste
# (c) Martin Guggisberg 2012

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

a=q[0][0]
print a

deflist =q[1]
print deflist

h=q[len(q)-1][len(q[len(q)-1])-1]
print h

#einfacher
h2 =q[-1][-1]
print h2


d = q[1][0]
print d

g =q[-1][-2]
print g
