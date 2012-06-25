
# Umrechnung von Fahrenheit in Grad Celsius
# (c) Martin Guggisberg 2012


# Aus dem Skript (Seite 41)
def F(C):
    return (9.0/5)*C+32

def C(F):
    return (F-32)*5.0/9.0


print '%g Grad Fahrenheit sind %g Grad Celsius'%(41,C(41))
print '%g Grad Celsisus sind %g Grad Fahrenheit' %(C(41),F(C(41)))
