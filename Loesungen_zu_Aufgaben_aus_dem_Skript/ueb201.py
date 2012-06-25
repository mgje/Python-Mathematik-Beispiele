
# Fahrenheit-Celsius Umwandlungstabelle
# (c) Martin Guggisberg 2012

print "Temp F      Temp C"
for F in range(101):
    C = 5.0/9.0*(F-32)
    print '%5d %5.1f' % (F, C)
