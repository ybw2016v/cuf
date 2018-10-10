#!/usr/bin/env python3
import numpy as np
import numpy.ctypeslib as npct
import ctypes
from ctypes import c_int
from ctypes import c_float
import time
from matplotlib import pyplot as plt
import math

M=1024
N=1024
libcd = npct.load_library("calkel", ".")
array_1d_double = npct.ndpointer(dtype=np.float32, ndim=2, flags='CONTIGUOUS')
p0=np.zeros([M,N],dtype=np.float32)
vx=np.zeros([M,N],dtype=np.float32)
vz=np.zeros([M,N],dtype=np.float32)
z=np.ones([M,N],dtype=np.float32)
libcd.cal.argtypes=[array_1d_double,array_1d_double,array_1d_double,array_1d_double,c_int,c_int,c_int,c_int,c_int,c_float,c_int]
libcd.cal.restype=c_int
ff=np.array(p0.strides,dtype='int32')
dd=np.array(np.shape(p0),dtype='int32')
# print(p0)
# print(ff[1],ff[0],dd[1],dd[0])
ts=time.time()
libcd.cal(p0,vx,vz,z,ff[1],ff[0],dd[1],dd[0],10000,9,0)
# libcd.sdogkel.argtypes=[c_int]
# libcd.sdogkel(5)
# for itime in range(1,10000):
#     p0[200,200]=math.sin(itime)
#     libcd.cal(p0,vx,vz,z,ff[1],ff[0],dd[1],dd[0],1,9,0)
#     pass
te=time.time()
time.sleep(0.5)
# print(p0)
print("gpu:"+str(te-ts))
p0[200,200]=0
# plt.figure()
# plt.imshow(p0[:,:])
# plt.colorbar()
# plt.show()