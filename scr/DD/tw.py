#!/usr/bin/env python3
import numpy as np
import numpy.ctypeslib as npct
import ctypes
from ctypes import c_int
import time

libcd = npct.load_library("cutwo", ".")
array_1d_double = npct.ndpointer(dtype=np.float32, ndim=2, flags='CONTIGUOUS')
Datdog=np.ones([4096,1024],dtype=np.float32)
Datdog2=np.ones([4096,1024],dtype=np.float32)
# print(Datdog)
# libcd.floatprint.argtypes=[array_1d_double,c_int,c_int,c_int,c_int]
# libcd.floatprint.restype=c_int
# ff=np.array(Datdog.strides,dtype='int32')
# dd=np.array(np.shape(Datdog),dtype='int32')
# libcd.floatprint(Datdog,ff[1],ff[0],dd[1],dd[0])
# print(dd[1])
ts1=time.time()
libcd.cucaldog.argtypes=[array_1d_double,c_int,c_int,c_int,c_int]
libcd.cucaldog.restype=c_int
ff=np.array(Datdog.strides,dtype='int32')
dd=np.array(np.shape(Datdog),dtype='int32')
libcd.cucaldog(Datdog,ff[1],ff[0],dd[1],dd[0])
te1=time.time()
ts2=time.time()
for idog in range(0,dd[0]):
    for jdog in range(0,dd[1]):
        Datdog2[idog,jdog]=(idog+jdog)*(idog-jdog)
        pass
    pass
te2=time.time()
t1=te1-ts1
t2=te2-ts2
print('gpu'+str(t1)+'\ '+'cpu'+str(t2)+'加速比：'+str(t2/t1))
# print(Datdog)
