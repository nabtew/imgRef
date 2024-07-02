from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds
from PySide2 import QtUiTools
import os
import sys
import imgRef_icons #icons ไฟล์
import Utility_imgRef as uti 
from importlib import reload 
reload (uti)

moduleDir = os.path.dirname(sys.modules[__name__].__file__)
maya_ptr = omui.MQtUtil.mainWindow()
ptr = wrapInstance(int(maya_ptr), QWidget)
myUiFile = '%s\\impRef_v2.ui' %moduleDir
widgetUiFile = '%s\\widget_Import.ui' %moduleDir

def setup_ui_maya(uiFile, parent):
    """Qt Module to load .ui file"""
    # read .ui directly
    moduleDir = os.path.dirname(uiFile)
    loader = QtUiTools.QUiLoader()
    loader.setWorkingDirectory(moduleDir)

    f = QFile(uiFile)
    f.open(QFile.ReadOnly)

    myWidget = loader.load(f, parent)
    f.close()

    return myWidget

mainUi = setup_ui_maya(myUiFile, ptr)

    # Directory of your .ui file

def run():
    global mainUi
    try:
        mainUi.close()
    except:
        pass

    mainUi.show()

def check_selected_button():
    action_cam = ""
    selection_check_cam = cmds.ls(sl=True)
    if mainUi.createCam_button.isChecked():
        action_cam = uti.usr_create_cam(mainUi.name_box.text())

    elif mainUi.selectCam_button.isChecked():

        for obj in selection_check_cam:
            shape_nodes = cmds.listRelatives(obj, shapes=True) or []
            for shape in shape_nodes:
                node_type = cmds.nodeType(shape)
                if node_type == "camera":
                    action_cam = uti.cam_selected()

    else :
        print("plsss select your camera naka")
    
    return action_cam
            
def test_createCam_button():
    if mainUi.createCam_button.isChecked():
        mainUi.selectCam_button.setChecked(False)

def test_selectCam_button():
    if mainUi.selectCam_button.isChecked():
        mainUi.createCam_button.setChecked(False)

widgetUi = setup_ui_maya(widgetUiFile, ptr)
mainUi.createCam_button.clicked.connect(test_createCam_button)
mainUi.selectCam_button.clicked.connect(test_selectCam_button)
mainUi.ok_button.clicked.connect(lambda: uti.mainUtility(check_selected_button()))
mainUi.Q_button.clicked.connect(lambda: widgetUi.show())