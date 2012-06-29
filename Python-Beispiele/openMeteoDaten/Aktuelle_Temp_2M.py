"""
plot H's and L's on a sea-level pressure map
(uses scipy.ndimage.filters and netcdf4-python)
"""
import numpy as np
import matplotlib.pyplot as pp
import sys
from datetime import datetime, timedelta
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid, cm
from scipy.ndimage.filters import minimum_filter, maximum_filter
from netCDF4 import Dataset 


# set date (yesterday at 00 UTC)
YYYYMMDDHH = (datetime.now()-timedelta(1)).strftime('%Y%m%d')+'00'

# open OpenDAP dataset.
data=Dataset("http://nomad2.ncep.noaa.gov:9090/dods/gdas/rotating/gdas"+YYYYMMDDHH+".grib2")

#data=Dataset("http://nomad2.ncep.noaa.gov:9090/dods/gdas/rotating/gdas2012051900.grib2")

# read lats,lons.
lats = data.variables['lat'][:]
lons1 = data.variables['lon'][:]
nlats = len(lats)
nlons = len(lons1)
# read tmax 2m (K).
tmax2m = data.variables['tmax2m'][0]-273.15
# shift data so lons go from -180 to 180 instead of 20 to 380.
tmax2m,lons1 = shiftgrid(180.,tmax2m,lons1,start=False)



# create Basemap instance.
m = Basemap(llcrnrlon=-180,llcrnrlat=-80,urcrnrlon=180,urcrnrlat=80,projection='mill')
# add wrap-around point in longitude.
tmax2m, lons = addcyclic(tmax2m, lons1)
# contour levels
clevs = np.arange(-39.,42.,1.)
# find x,y of map projection grid.
lons, lats = np.meshgrid(lons, lats)
x, y = m(lons, lats)
# create figure.
fig=pp.figure(figsize=(16,9))
ax = fig.add_axes([0.05,0.05,0.9,0.85])
cs = m.contourf(x,y,tmax2m,clevs,shading='flat',cmap=pp.cm.jet)
m.drawcoastlines(linewidth=1.25)
#m.fillcontinents(color='0.8')
m.drawparallels(np.arange(-80,81,20),labels=[1,1,0,0])
m.drawmeridians(np.arange(0,360,60),labels=[0,0,0,1])

c = pp.colorbar(cs,orientation='horizontal')
pp.title('Temperature in [C] %s' % YYYYMMDDHH)
pp.savefig('wetterlage.png')
pp.show()
