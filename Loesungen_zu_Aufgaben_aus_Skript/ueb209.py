
# Berechnung eines beliebigen Polynoms
# (c) Martin Guggisberg 2012



x = 0.5
R = [-1,1,2]
p = 1.0

for r in R:
    p = p*(x-r)

print p
