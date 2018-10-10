#!/usr/bin/env python3
import argparse
import os
import shutil
from argparse import RawTextHelpFormatter

import numpy as np

parser = argparse.ArgumentParser(description='NPY格式数组生成器\n默认数值为1\n例子：\n生成一个2X3的名为“num”二维数组:\n./initdog.py -2d -name num 2 3\n生成一个2X3X4的数值为5.3的三维数组：\n/initdog.py -3d -n 5.3 2 3 4',formatter_class=RawTextHelpFormatter)
group = parser.add_mutually_exclusive_group()
group.add_argument('-2d','--d2',help='二维',action="store_true")
group.add_argument('-3d','--d3',help='三维',action="store_true")
parser.add_argument('-name',help='输出文件名',nargs='?',default='dogz')
parser.add_argument('-n',help='数值',type=float,nargs='?',default=1.0)
parser.add_argument('x',type=int,help='X轴',nargs=1)
parser.add_argument('y',type=int,help='Y轴',nargs=1)
parser.add_argument('z',type=int,help='Z轴',nargs='?')
args = parser.parse_args()

if args.d2:
    # print(args.n)
    a=np.ones([args.x[0],args.y[0]],dtype='float32')
    a[:,:]=a[:,:]*float(args.n)
    # print(np.shape(a))
    np.save(args.name,a)
    pass

if args.d3:
    a=np.ones([args.x[0],args.y[0],args.z],dtype='float32')
    a[:,:,:]=a[:,:,:]*float(args.n)
    np.save(args.name,a)
    pass


# a=np.ones([256,256,80],dtype='float32')
# a[80:120,90:100,20:70]=0
# np.save('dogz',a)
