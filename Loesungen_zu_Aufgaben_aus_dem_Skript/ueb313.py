
# Max / Min
# (c) Martin Guggisberg 2012


l=[1.2,2,3.1,1.1,5.1,2.1,3,1.1,2.11,3,3.1,0.9,0.85,0.9]

max_element=l[0]
min_element=l[0]
for e in l[1:]:
    if e > max_element:
        max_element=e
    if e < min_element:
        min_element=e

print "Maximum: %g"%max_element
print "Minimum: %g"%min_element

