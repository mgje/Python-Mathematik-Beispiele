import time
import sys
import matplotlib.pyplot as pp
import random
 
if sys.platform == "win32":
     # On Windows, the best timer is time.clock()
     default_timer = time.clock
else:    
    # On most other platforms the best timer is time.time()    
    default_timer = time.time
     
     
# generate ends for the line segments
xpairs = []
ypairs = []
for i in range(1000):
    xends = [random.random(), random.random()]
    yends = [random.random(), random.random()]
    xpairs.append(xends)
    ypairs.append(yends)
 
############################
# time sequential call to matplotlib
pp.figure()
pp.subplot(1,3,1)
 
t0 = default_timer()
for xends,yends in zip(xpairs,ypairs):
    pp.plot(xends,yends,'b-',alpha=0.1)
t1 = default_timer()
 
pp.title('Sequential Plotting')
 
print 'Execution time for sequential plotting = %f sec' % (t1-t0)
 
############################
# build argument list
call_list = []
for xends,yends in zip(xpairs,ypairs):
    call_list.append(xends)
    call_list.append(yends)
    call_list.append('-b')
     
############################
# time single call to matplotlib
pp.subplot(1,3,2)
 
t0 = default_timer()
pp.plot(*call_list,alpha=0.1)
t1 = default_timer()
 
pp.title('Single Plot extended call')
 
print 'Execution time for extended call plotting = %f sec' % (t1-t0)
 
############################
# rebuild ends using none to separate line segments
xlist = []
ylist = []
for xends,yends in zip(xpairs,ypairs):
    xlist.extend(xends)
    xlist.append(None)
    ylist.extend(yends)
    ylist.append(None)
     
############################
# time single call to matplotlib
pp.subplot(1,3,3)
 
t0 = default_timer()
pp.plot(xlist,ylist,'b-',alpha=0.1)
t1 = default_timer()
 
pp.title('Single Plot Using None')
 
print 'Execution time when using None = %f sec' % (t1-t0)
 
pp.show()
