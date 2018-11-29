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





class DogPlotres(HasTraits):


    scene = Instance(MlabSceneModel, ())
    ImportDog =  Button("导入")
    DogImpor=Directory('./res/')

    DogName=Str('p0_0.npy')

    MeenDog=Enum(['点图','等值面'])
    Num=0

    DogNext =  Button("下一个")

    DogNext2 =  Button("上一个")

    DogNum =Int(15)

    DogNummax =Float(2)
    DogNummin =Float(-2)

    Plot =  Button("绘图")



    dog=Item(name='scene',editor=SceneEditor(scene_class=MayaviScene),resizable=True,height=600,width=800)

    view=View(HGroup(dog,VGroup(Item(name='DogImpor',label='导入目录'),Item(name='ImportDog',label='导入'),Item(name='DogName',label='文件名'),Item(name='MeenDog',label='类别'),Item(name='DogNum',label='等值面数量'),Item(name='DogNummax',label='等值面最大值'),Item(name='DogNummin',label='等值面最小值'),Item(name='DogNext',label='下一个'),Item(name='DogNext2',label='上一个')),'Plot',show_labels=False),resizable = True,title=u"TraitsUI",buttons=OKCancelButtons)

    def _ImportDog_fired(self):
        self.LsbDog=np.load(str(self.DogImpor)+str(self.DogName))

        pass

    def _Plot_fired(self, parameter_list):
        self.ploot()

        pass
    def _DogNext_fired(self):
        self.Num=self.Num+1
        self.DogName='p0_'+str(self.Num)+'.npy'
        self.LsbDog=np.load(str(self.DogImpor)+str(self.DogName))
        self.ploot()

        pass
    def _DogNext2_fired(self):
        self.Num=self.Num-1
        self.DogName='p0_'+str(self.Num)+'.npy'
        self.LsbDog=np.load(str(self.DogImpor)+str(self.DogName))
        self.ploot()
        pass
    def ploot(self):
        if self.MeenDog=='点图':
            a,b,c=self.LsbDog.shape
            mlab.clf()
            mlab.contour3d(self.LsbDog[2:int(a-4),2:int(b-4),2:int(c-4)],contours=int(self.DogNum),vmax=float(self.DogNummax),extent=[0,a,0,b,0,c],vmin=float(self.DogNummin),transparent=True)
            mlab.axes(xlabel='x', ylabel='y', zlabel='z')
            mlab.colorbar()
        else:
            mlab.clf()
            fileddog=mlab.pipeline.scalar_field(self.LsbDog)
            mlab.pipeline.volume(fileddog)
            mlab.axes(xlabel='x', ylabel='y', zlabel='z')
            mlab.colorbar()
        pass



    pass


app = DogPlotres(resizable=True)
app.configure_traits()   