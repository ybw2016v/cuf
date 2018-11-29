
import numpy as np
from mayavi import mlab

ddd= np.load('p0_0.npy')
# ddd[1,1:81,1:81]=6
# ddd[:,1,:]=6
fileddog=mlab.pipeline.scalar_field(ddd)
# mlab.pipeline.volume(fileddog)
# 
print(ddd.shape)
mlab.contour3d(ddd,contours=20,transparent=True)
mlab.colorbar()
mlab.show()