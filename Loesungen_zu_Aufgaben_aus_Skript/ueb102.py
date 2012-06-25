# Umwandlung in britische Einheiten
# (c) Martin Guggisberg 2012

g = 640.0   # in [m]

inch = 0.0254    # in [m]
fuss = inch*12   # in [m]
yard = fuss*3    # in [m]
meile = yard*1760 # in [m]

print "%g m entspricht mit %g Inches, %g Feet, %g Yards oder %g Miles." % (g,g/inch,g/fuss,g/yard,g/meile)


