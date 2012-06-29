from netCDF4 import Dataset
import numpy as np

root_grp = Dataset('test.nc', 'w', format='NETCDF4')
root_grp.description = 'Example temperature data'

# dimensions
root_grp.createDimension('time', None)
root_grp.createDimension('lat', 72)
root_grp.createDimension('lon', 144)

# variables
times = root_grp.createVariable('time', 'f8', ('time',))
latitudes = root_grp.createVariable('latitude', 'f4', ('lat',))
longitudes = root_grp.createVariable('longitude', 'f4', ('lon',))
temp = root_grp.createVariable('temp', 'f4', ('time', 'lat', 'lon',))

# data
lats =  np.arange(-90, 90, 2.5)
lons =  np.arange(-180, 180, 2.5)
latitudes[:] = lats
longitudes[:] = lons
for i in range(5):
    temp[i,:,:] = np.random.uniform(size=(len(lats), len(lons)))

root_grp.close()