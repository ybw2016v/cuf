#!/usr/bin/env python3

from traitsui.api import Item, RangeEditor, View
from traits.api import HasTraits, Str, Range, Enum, Int

from traits.api import *
from traitsui.api import *
from tvtk.pyface.scene_editor import SceneEditor 
from mayavi.tools.mlab_scene_model import MlabSceneModel
from mayavi.core.ui.mayavi_scene import MayaviScene




view1 = View(
    Item(name='scene', 
                editor=SceneEditor(scene_class=MayaviScene), # 设置mayavi的编辑器
                resizable=True,
                height=250,
                width=400
            ),
    Item(name = 'department', label=u"部门", tooltip=u"在哪个部门干活"),
    Item(name = 'last_name', label=u"姓"),
    Item(name = 'first_name', label=u"名"), resizable = True,
    width = 400,
    height = 150)

class SimpleEmployee(HasTraits):
    first_name = Str
    last_name = Str
    department = Str
    employee_number = Str
    salary = Int
    plotbutton = Button(u"绘图")
    scene = Instance(MlabSceneModel, ()) # mayavi场景

sam = SimpleEmployee()
sam.configure_traits(view=view1)