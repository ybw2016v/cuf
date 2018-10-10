#!/usr/bin/env python3
import numpy as np
import numpy.ctypeslib as npct
import ctypes
from ctypes import c_int
import time
from matplotlib import pyplot as plt

libcd = npct.load_library("cutwo", ".")
array_1d_double = npct.ndpointer(dtype=np.float32, ndim=2, flags='CONTIGUOUS')
p0=np.ones([400,400],dtype=np.float32)
vx=np.ones([400,400],dtype=np.float32)
vz=np.ones([400,400],dtype=np.float32)
z=np.ones([400,400],dtype=np.float32)
libcd.sdoginit.argtypes=[array_1d_double,array_1d_double,array_1d_double,array_1d_double,c_int,c_int,c_int,c_int,c_int]
libcd.sdoginit.restype=c_int
ff=np.array(p0.strides,dtype='int32')
dd=np.array(np.shape(p0),dtype='int32')
print(p0)
libcd.sdoginit(p0,vx,vz,z,ff[1],ff[0],dd[1],dd[0],1200)
libcd.sdogkel.argtypes=[c_int]
# libcd.sdogkel(5)
time.sleep(0.5)
print(p0)
p0[200,200]=0
plt.figure()
plt.imshow(p0[:,:])
plt.colorbar()
plt.show()