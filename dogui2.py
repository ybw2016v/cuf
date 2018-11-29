#!/usr/bin/env python3

import numpy as npy
import numpy as np
from mayavi import mlab
from mayavi.core.ui.mayavi_scene import MayaviScene
from mayavi.tools.mlab_scene_model import MlabSceneModel
from traits.api import *
from traits.api import Enum, HasTraits, Int, Range, Str
from traitsui.api import *
from traitsui.api import Item, RangeEditor, View
from traitsui.menu import *
from tvtk.pyface.scene_editor import SceneEditor

from stl2vol import *


class DogPlot(HasTraits):
    SaveDog = Button(u"绘图测试")
    PDog = Button("绘图")
    ImportDog =  Button("导入")
    DogClf = Button("清除绘图")
    scene = Instance(MlabSceneModel, ()) # mayavi场景
    DogsName = File('cat3.stl')
    DogNumber = Int(50)
    DogOutP = File('out')
    DogOutC = File('outc.c')
    DogInter = Float('1.0')
    DogOutShape = Str
    DogOutput = Button("导出")
    DogCal = Button("计算")
    # DogButtons=OKButton
    D0 = Float(1)
    D0s = Bool
    D1 = Float(2)
    D1s = Bool
    D2 = Float(3)
    D2s = Bool
    D3 = Float(4)
    D3s =Bool
    D4 = Float(5)
    D4s = Bool
    D5 = Float(6)
    D5s = Bool
    D6 = Float(7)
    D6s = Bool
    D7 = Float(8)
    D7s =Bool
    D8 = Float(9)
    D8s = Bool
    DogC=Str
    gdc=Item(name='DogC',style='custom',label='输出预览',resizable=True,height=600,width=400)
    gd=[Item(name='D0'),Item(name='D0s'),Item(name='D1'),Item(name='D1s'),Item(name='D2'),Item(name='D2s'),Item(name='D3'),Item(name='D3s'),Item(name='D4'),Item(name='D4s'),Item(name='D5'),Item(name='D5s'),Item(name='D6'),Item(name='D6s'),Item(name='D7'),Item(name='D7s'),Item(name='D8'),Item(name='D8s')]



    out=[Item(name='DogOutP',label='npy输出'),Item(name='DogOutC',label='C输出文件名'),Item(name='DogInter',label='插值系数'),Item(name='DogCal',label='计算'),Item(name='DogOutShape',label='输出规模',style='readonly'),Item(name='DogOutput',label='导出')]
    view = View(
        HSplit(VSplit(gdc),VGroup(
            Item(name='scene', 
                editor=SceneEditor(scene_class=MayaviScene), # 设置mayavi的编辑器
                resizable=True,
                height=600,
                width=800
            ),
            'SaveDog','PDog','DogClf',
            show_labels=False
        ),
        VSplit(VGroup(Item(name='DogsName',label='文件名'),Item(name='DogNumber',label='解析度'),Item(name='ImportDog',label="导入STL模型")),VGroup(out),VGroup(gd)),
        
    ),resizable = True,title=u"TraitsUI",buttons=OKCancelButtons)
    def _SaveDog_fired(self):
        self.plot()
    def _PDog_fired(self):
        self.lu.DogPlot()
    def _ImportDog_fired(self):
        mlab.clf()
        self.lu=StlDog(self.DogsName,self.DogNumber)
        self.DogOutShape=str(self.lu.OutDog.shape)
        pass
    def _DogClf_fired(self):
        mlab.clf()
        # self.D0=self.D0+1
        pass
    def plot(self):
        mlab.clf()
        g = self.scene.mlab.test_mesh()
        # CloseAction()
    def _DogCal_fired(self):
        self.Doga1=npy.zeros_like(self.lu.cutdog)
        self.NewDog=self.lu.cutdog.copy()
        # print(self.DogInter)
        self.NBdog=int3dog(self.lu.cutdog,(float(self.DogInter)))
        print(self.NBdog.shape)
        # self.NBdog
        # np.save('cccog',self.lu.cutdog)
        # np.save('dddog',self.NBdog)
        mlab.clf()
        fileddog=mlab.pipeline.scalar_field(self.NBdog)
        self.nummax=self.NBdog.max()
        self.DogOutShape=str(self.NBdog.shape)
        mlab.pipeline.volume(fileddog,vmin=0,vmax=self.nummax)
        # mlab.contour3d(self.NBdog)
        mlab.colorbar()
        self.DogNpy()
        self.DogCwj()

        

        # FunDog=npy.frompyfunc(self.Dogcov,2,0)
        # FunDog(self.Doga1,self.lu.OutDog)
        pass
    def DogNpy(self):
        ###生成npy
        self.SsbDog=self.NBdog.copy()
        self.nul=[self.D0,self.D1,self.D2,self.D3,self.D4,self.D5,self.D6,self.D7,self.D8]
        fufdog=self.NBdog.reshape(-1) #成行
        dudog=self.SsbDog.reshape(-1)
        for usbdog in range(0,9):
            lsb=np.argwhere(fufdog==usbdog)
            dudog[lsb]=float(self.nul[usbdog])
            pass
    def DogCwj(self):
        #生成C文件
        DogStr=r'''    static int x$num[]=$rx1;
    static int y$num[]=$ry1;
    static int z$num[]=$rz1;
    int longdog=$l1;
    for (int icd = 0; icd  < longdog; icd ++)
    {
        //p1[x$num[icd]*xar+y$num[icd]*yar+z$num[icd]*zar]=
        //vx[x$num[icd]*xar+y$num[icd]*yar+z$num[icd]*zar]=
        //vy[x$num[icd]*xar+y$num[icd]*yar+z$num[icd]*zar]=
        //vz[x$num[icd]*xar+y$num[icd]*yar+z$num[icd]*zar]=
        //z0[x$num[icd]*xar+y$num[icd]*yar+z$num[icd]*zar]=
    }
    '''

        self.nuls=[self.D0s,self.D1s,self.D2s,self.D3s,self.D4s,self.D5s,self.D6s,self.D7s,self.D8s]
        cumdog='\n'
        for chDog in range(0,9):
            # print(chDog)
            if self.nuls[chDog]==True:
                lup=np.where(self.NBdog==chDog)
                # llxx=len()
                spx1=str(list(lup[1]))
                spy1=str(list(lup[2]))
                spz1=str(list(lup[0]))
                spl=str(lup[0].size)
                spx=self.DogStr(spx1)
                spy=self.DogStr(spy1)
                spz=self.DogStr(spz1)
                apu=DogStr.replace('$num',str(chDog)).replace('$rx1',spx).replace('$ry1',spy).replace('$rz1',spz).replace('$l1',spl)
                cumdog=cumdog+apu
                print(chDog)
            pass
        pass
        esodog='''
void usercode(float * p1,float * vx,float * vy,float * vz,float *z0,int xar, int yar,int zar,float m,int i)
{

$0$

}
        '''
        self.DogC=esodog.replace('$0$',cumdog)
        


        pass
    def Dogcov(self,a,b):
        self.nul=[self.D0,self.D1,self.D2,self.D3,self.D4,self.D5,self.D6,self.D7,self.D8]
        for idog in range(0,8):
            if self.b==idog:
                self.a=self.nul[idog]
            pass
        pass    
    def _DogOutput_fired(self):
        np.save(self.DogOutP,self.SsbDog)
        with open(self.DogOutC, 'w+',encoding='utf-8') as f:
            f.write(self.DogC)
        pass
    
    def DogStr(self,strindog):
        luf=len(strindog)
        cudog='{'+strindog[1:luf-1]+'}'
        return cudog
        pass



app = DogPlot(resizable=True)
app.configure_traits()   
