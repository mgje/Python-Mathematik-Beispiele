
# x-Koordinaten mit gleichem Abstand
# (c) Martin Guggisberg 2012


abst= 0.01
end= 2.0
x = 1.00
k1 = []

while (x <= end):
    k1.append(x)
    x=x+abst

print k1

# Besser

abst= 0.01
end= 2.0
x = 1.00

k1 = []

schritte = int((end-x)/abst + 1) # Gartenhag, n Zwischenräume , n+1 Pfosten

for i in range(schritte):
    k1.append(x)
    x=x+abst


print k1
