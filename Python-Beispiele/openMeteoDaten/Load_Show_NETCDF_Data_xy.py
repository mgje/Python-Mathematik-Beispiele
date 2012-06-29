from netCDF4 import Dataset
import matplotlib.pyplot as pp

root_grp = Dataset('test.nc')

temp = root_grp.variables['temp']
fn=''
for i in range(len(temp)):
# clear figure
    pp.clf()
# contour plot  
    pp.contourf(temp[i])
    fn='random_'+str(i)+'.png'
    pp.savefig(fn)
    pp.show()
    
