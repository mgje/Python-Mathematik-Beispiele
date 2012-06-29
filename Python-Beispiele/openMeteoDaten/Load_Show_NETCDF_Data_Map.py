from netCDF4 import Dataset
import matplotlib.pyplot as pp
from mpl_toolkits.basemap import Basemap, cm
import numpy as np

root_grp = Dataset('test.nc')
temp = root_grp.variables['temp']
lons = root_grp.variables['longitude'][:]
lats = root_grp.variables['latitude'][:]
nx=len(lats)
ny=len(lons)

fig=pp.figure(figsize=(16,20))
# set up orthographic map projection with
# perspective of satellite looking down at 50N, 100W.
# use low resolution coastlines.
map = Basemap(projection='ortho',lat_0=45,lon_0=20,resolution='l')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color='coral',lake_color='aqua')
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='aqua')

# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))



topodat = map.transform_scalar(temp[0],lons,lats,nx,ny)
im = map.imshow(topodat,cm.GMT_haxby,alpha=0.85)

c = pp.colorbar(im,orientation='horizontal')
pp.title('map the world')
pp.savefig('contour1.png')
pp.show()
