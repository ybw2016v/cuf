#!/usr/bin/env python3
import sys
sys.setrecursionlimit(100000000)
import numpy as np
from mesh_vox import read_and_reshape_stl, voxelize
import math
from mayavi import mlab

def stltrdog(stlpath,resolution):



    mesh, bounding_box = read_and_reshape_stl(stlpath, resolution)

    voxels, bounding_box = voxelize(mesh, bounding_box)
    resdog=voxels.transpose((2,1,0))
    return resdog
    pass

def showdog(sdog):
    pug=np.zeros_like(sdog,dtype='float32')
    for idog in range(0,np.shape(sdog)[0]):
        for jdog in range(0,np.shape(sdog)[1]):
            for kdog in range(0,np.shape(sdog)[2]):
                if sdog[idog,jdog,kdog]==True:
                    # print("OK")
                    pug[idog,jdog,kdog]=1
                    pass
                else:
                    pug[idog,jdog,kdog]=0
                    pass
    # mlab.imshow(pug[:,:,20])
    # 


    fileddog=mlab.pipeline.scalar_field(pug)
    mlab.pipeline.volume(fileddog,vmin=0,vmax=3)
    mlab.colorbar()
    mlab.show()
    pass

def devidedog(sdog):
    pug=np.zeros_like(sdog,dtype='float32')
    a=np.where(sdog==True)
    numdog=1
    while np.where(sdog==True)[0].shape[0]!=0:
        cut=[np.where(sdog==True)[0][0],np.where(sdog==True)[1][0],np.where(sdog==True)[2][0]]
        diguidog2(sdog,pug,cut[0],cut[1],cut[2],numdog)
        numdog=numdog+1
        # print(numdog)
        pass
    return pug,numdog
    pass

def diguidog(acat,bcat,idog,jdog,kdog,intdog):
    if idog>=1 and idog<=(acat.shape[0]-2) and jdog>=1 and jdog<=(acat.shape[1]-2) and kdog>=1 and kdog<=(acat.shape[2]-2):
        if acat[idog,jdog,kdog]==True:
            bcat[idog,jdog,kdog]=intdog
            acat[idog,jdog,kdog]=False
            # print(idog,jdog,kdog)
            if acat[idog+1,jdog,kdog]==True:
                diguidog(acat,bcat,idog+1,jdog,kdog,intdog)
            if acat[idog-1,jdog,kdog]==True:
                diguidog(acat,bcat,idog-1,jdog,kdog,intdog)
            if acat[idog,jdog+1,kdog]==True:
                diguidog(acat,bcat,idog,jdog+1,kdog,intdog)
            if acat[idog,jdog-1,kdog]==True:
                diguidog(acat,bcat,idog,jdog-1,kdog,intdog)
            if acat[idog,jdog,kdog+1]==True:
                diguidog(acat,bcat,idog,jdog,kdog+1,intdog)
            if acat[idog,jdog,kdog-1]==True:
                diguidog(acat,bcat,idog,jdog,kdog-1,intdog)
            pass
        else:
            # print('end')
            pass
    else:
        # print("out")
        pass
    return 0

    pass


def diguidog2(acat,bcat,idog,jdog,kdog,intdog):

    pflodog=acat[idog,jdog,kdog]
    if pflodog==True:
        # flagdog=6
        pass
    else:
        # flagdog=0
        pass
    hu=[[idog,jdog,kdog]]
    du=[]
    num=1
    while hu!=[]:
        # flagdog=6
        for ludog in hu:
            bcat[ludog[0],ludog[1],ludog[2]]=intdog
            acat[ludog[0],ludog[1],ludog[2]]=False
            if acat[ludog[0]+1,ludog[1],ludog[2]]==True and ludog[0]+1<=(acat.shape[0]-2):
                if [ludog[0]+1,ludog[1],ludog[2]] in du:
                    # print('重复')
                    pass
                else:
                    du.append([ludog[0]+1,ludog[1],ludog[2]])
                    pass
                pass
            else:
                # flagdog=flagdog-1
                pass
            if acat[ludog[0],ludog[1]+1,ludog[2]]==True and ludog[1]+1<=(acat.shape[1]-2):
                if [ludog[0],ludog[1]+1,ludog[2]] in du:
                    pass
                else:
                    du.append([ludog[0],ludog[1]+1,ludog[2]])
                    pass
                
                pass
            else:
                # flagdog=flagdog-1
                pass

            if acat[ludog[0],ludog[1],ludog[2]+1]==True and (ludog[2]+1)<=(acat.shape[2]-2) and not ([ludog[0],ludog[1],ludog[2]+1] in du):
                du.append([ludog[0],ludog[1],ludog[2]+1])
                pass
            else:
                # flagdog=flagdog-1
                pass


            if acat[ludog[0]-1,ludog[1],ludog[2]]==True and ludog[0]-1>=(0)and not([ludog[0]-1,ludog[1],ludog[2]] in du):
                du.append([ludog[0]-1,ludog[1],ludog[2]] )
                pass
            else:
                # flagdog=flagdog-1
                pass


            if acat[ludog[0],ludog[1]-1,ludog[2]]==True and ludog[1]-1>=(0) and not([ludog[0],ludog[1]-1,ludog[2]] in du):
                du.append([ludog[0],ludog[1]-1,ludog[2]]  )
                pass
            else:
                # flagdog=flagdog-1
                pass

            if acat[ludog[0],ludog[1],ludog[2]-1]==True and ludog[2]-1>=(0) and not([ludog[0],ludog[1],ludog[2]-1] in du):
                du.append([ludog[0],ludog[1],ludog[2]-1])
                pass
            else:
                # flagdog=flagdog-1
                pass
            pass
        hu=du
        du=[]
        print(hu.__len__())
        num=num+1
        pass
            
        

        pass



    pass

def puttdog(sfdog):
    mlab.clf()
    cutdog,numpug=devidedog(sfdog)
    fileddog=mlab.pipeline.scalar_field(cutdog)
    mlab.pipeline.volume(fileddog,vmin=0,vmax=numpug-1)
    mlab.colorbar()
    # mlab.show()


    pass

class StlDog(object):
    def __init__(self,Dogname,rse):
        self.Dogfile=Dogname
        self.DogRes=rse
        self.OutDog=stltrdog(self.Dogfile,self.DogRes)
        self.cutdog,self.numpug=devidedog(self.OutDog)
        
    def DogPlot(self):
        # puttdog(self.OutDog)
        mlab.clf()
        fileddog=mlab.pipeline.scalar_field(self.cutdog)
        mlab.pipeline.volume(fileddog,vmin=0,vmax=self.numpug-1)
        mlab.colorbar()
        pass
    pass

# dog=stltrdog('cat3.stl',800)
# puttdog(dog)