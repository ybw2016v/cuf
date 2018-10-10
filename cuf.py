#!/usr/bin/env python3
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-t','--type',help='计算类型',nargs='?',choices=['2d','2dm','3d','3dm'])
parser.add_argument('path',help='配置文件路径',default='cufig.ini',nargs='?')
# gu=parser.add_argument_group()
# gu.add_argument('-g','--generate',help='自动化生成初始网格文件',nargs='?')
# gu.add_argument('-dim',help='维度',choices=[3,2],type=int,nargs=1)
args = parser.parse_args()
# print(args.type)
# print(args.path)

def cal2d(path):
    shutil.copyfile('./scr/DD/Makefile','Makefile')
    shutil.copyfile('./scr/DD/calkel.cu','calkel.cu')
    shutil.copyfile('./scr/DD/culib.py','culib.py')
    # os.system('make')
    import culib
    a = culib.decodeconf(path)
    cat=culib.caldog(a)
    cat.loadlib('')
    cat.cal()
    pass

def cal2dm(path):
    shutil.copyfile('./scr/DDmur/Makefile','Makefile')
    shutil.copyfile('./scr/DDmur/calkel.cu','calkel.cu')
    shutil.copyfile('./scr/DDmur/culib.py','culib.py')
    # os.system('make')
    import culib
    a = culib.decodeconf(path)
    cat=culib.caldog(a)
    cat.loadlib('')
    cat.cal()
    pass
def cal3d(path):
    shutil.copyfile('./scr/DDD/Makefile','Makefile')
    shutil.copyfile('./scr/DDD/calkel3.cu','calkel3.cu')
    shutil.copyfile('./scr/DDD/culib3.py','culib3.py')
    import culib3
    a = culib3.decodeconf(path)
    cat=culib3.caldog(a)
    cat.loadlib('')
    cat.cal()
    pass
def cal3dm(path):
    shutil.copyfile('./scr/DDDmur/Makefile','Makefile')
    shutil.copyfile('./scr/DDDmur/calkel3.cu','calkel3.cu')
    shutil.copyfile('./scr/DDDmur/culib3.py','culib3.py')
    import culib3
    a = culib3.decodeconf(path)
    cat=culib3.caldog(a)
    cat.loadlib('')
    cat.cal()
    pass

def autocls():
    os.remove('Makefile')
    # os.remove('calkel.cu')
    os.system('rm cal*.cu')
    os.system('rm cul*.py')
    os.system('rm *.so')

print(args.path)
if args.type=='2d':
    cal2d(args.path)
if args.type=='2dm':
    cal2dm(args.path)
    pass
if args.type=='3d':
    cal3d(args.path)
if args.type=='3dm':
    cal3dm(args.path)
    pass



autocls()
