#!/usr/bin/env python3

import numpy as npy
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
    gd=[Item(name='D0'),Item(name='D0s'),Item(name='D1'),Item(name='D1s'),Item(name='D2'),Item(name='D2s'),Item(name='D3'),Item(name='D3s'),Item(name='D4'),Item(name='D4s'),Item(name='D5'),Item(name='D5s'),Item(name='D6'),Item(name='D6s'),Item(name='D7'),Item(name='D7s'),Item(name='D8'),Item(name='D8s')]



    out=[Item(name='DogOutP',label='npy输出'),Item(name='DogOutC',label='C输出文件名'),Item(name='DogInter',label='插值系数'),Item(name='DogCal',label='计算'),Item(name='DogOutShape',label='输出规模',style='readonly'),Item(name='DogOutput',label='导出')]
    view = View(
        HSplit(VGroup(
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
    def _DogCal_fired(self, parameter_list):
        self.Doga1=npy.zeros_like(self.lu.OutDog)
        
        pass
    def Dogcov(self,a,b):
        self.nul=[self.D0,self.D1,self.D2,self.D3,self.D4,self.D5,self.D6,self.D7,self.D8]
        for idog in range(0,9):
            if b==idog:
                self.a=self.nul[idog]
            pass
        pass    


app = DogPlot(resizable=True)
app.configure_traits()   
