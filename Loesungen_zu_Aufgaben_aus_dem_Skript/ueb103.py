# Wachstum von Geld auf einer Schweizer Bank
# (c) Martin Guggisberg 2012

p=1.5  # %
A=1000.0 # Euro
n = 3 # Jahre

guthaben = A*(1.0 + p/100.0)**n

print "Ihr Anfangsguthaben von %g waechst nach %d Jahre\
 auf den Wert von %g Euro" % (A,n,guthaben)


