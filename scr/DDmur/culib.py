#!/usr/bin/env python3
import configparser
import ctypes
import math
import time
import os
from ctypes import c_float, c_int

import numpy as np
import numpy.ctypeslib as npct
from matplotlib import pyplot as plt
from progressbar import *


def decodeconf(path):
    conf=configparser.ConfigParser()
    conf.read(path)
    reslist=[]
    selist=conf.sections()
    for dog in selist:
        reslist+=conf.items(dog)
    dic=dict(reslist)
    return dic

class caldog(object):
    def __init__(self, dic):
        conf=dic
        initz0 = conf['z0路径']
        self.z0=np.load(initz0)
        self.m=float(conf['m'])
        conf=dic
        self.outf=conf["输出频率"]
        self.N=conf['计算时间']
        # print(self.N)
        self.outpath=conf['输出路径']
        self.useraddpath=conf['添加方式']
        if self.z0.dtype == 'float32':
            print("OK")
        if conf['自动初值']=='是' or conf['自动初值']=='y' or conf['自动初值']=='y':
            print('开始自动生成')
            self.p0=np.zeros(np.shape(self.z0),dtype='float32')
            self.vx=np.zeros(np.shape(self.z0),dtype='float32')
            self.vz=np.zeros(np.shape(self.z0),dtype='float32')
            
            print('自动生成成功')
        else:
            initp0=conf['p0路径']
            self.p0=np.load(initp0)
            if self.z0.dtype == 'float32':
                print(str(initp0)+'导入成功')
            else:
                print("警告:数据类型错误。")
                    
            initvx=conf['vx路径']
            self.vx=np.load(initvx)
            if self.vx.dtype == 'float32':
                print(str(initvx)+'导入成功')
            else:
                print("警告:数据类型错误。")
            initvz=conf['vz路径']
            self.vz=np.load(initvz)
            if self.vz.dtype == 'float32':
                print(str(initvz)+'导入成功')
            else:
                print("警告:数据类型错误。")
        self.ff=np.array(self.p0.strides,dtype='int32')
        self.dd=np.array(np.shape(self.p0),dtype='int32')
        self.lx=np.zeros(2*self.dd[1],dtype='float32')
        self.lz=np.zeros(2*self.dd[0],dtype='float32')
        with open(self.useraddpath, 'r') as f:
            self.useradd=f.read()
        with open('calkel.cu','a+') as f:
            f.write(self.useradd)
        os.system('make')
        pass

    def loadlib(self,libp):
        
        self.libcd = npct.load_library("calkel", ".")
        array_1d_double = npct.ndpointer(dtype=np.float32, ndim=2, flags='CONTIGUOUS')
        array_1d_double2 = npct.ndpointer(dtype=np.float32, ndim=1, flags='CONTIGUOUS')
        self.libcd.cal.argtypes=[array_1d_double,array_1d_double,array_1d_double,array_1d_double,array_1d_double2,array_1d_double2,c_int,c_int,c_int,c_int,c_int,c_int,c_float,c_int]
        self.libcd.cal.restype=c_int
        pass
    def calcal(self,start,end):
        self.libcd.cal(self.p0,self.vx,self.vz,self.z0,self.lx,self.lz,self.ff[1],self.ff[0],self.dd[1],self.dd[0],start,end,self.m,0)
        pass

    def cal(self):
        a=int(int(self.N)/int(self.outf))
        b=int(self.N)%int(self.outf)
        c=0
        pbar = ProgressBar()
        for numtime in pbar(range(0,a)):
            self.calcal(c,c+int(self.outf))
            # print('*-'+str(c)+'-'+str(c+int(self.outf)))
            np.save(str(self.outpath)+'p0_'+str(numtime),self.p0)
            np.save(str(self.outpath)+'vx_'+str(numtime),self.vx)
            np.save(str(self.outpath)+'vz_'+str(numtime),self.vz)
            c=c+int(self.outf)
            pass
        self.calcal(c,c+b)
        np.save(self.outpath+'p0_'+str(a),self.p0)
        np.save(self.outpath+'vx_'+str(a),self.vx)
        np.save(self.outpath+'vz_'+str(a),self.vz)
        pass
    
    pass
