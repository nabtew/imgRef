
import maya.cmds as cmds
from PIL import Image

#ฟังก์ชั่นใช้เก็บรวบรวมและเรียกใช้ฟังก์ชั่นทั้งหมด
def mainUtility(selCam): #selCam คือพารามิเตอร์จาก running.py(ถูกเรียกใช้ในบรรทัดที่ 80)
    selected_camera = selCam #ตัวแปรของกล้องที่ผู้ใช้ต้องการใส่เรฟ
    imgPlane = new_imagePlane()
    set_seq(imgPlane[1])
    setAttr_parent(imgPlane[0], selected_camera)
    file_path = select_imp(imgPlane[1])
    width, height = get_image_dimensions(cmds.getAttr(imgPlane[1] + ".imageName"))
    size_manage(width, height, imgPlane)
    clear_tranImp(imgPlane[0])
    cmds.lookThru(selCam)

#สร้างกล้อง และ unhidden 
def usr_create_cam(cam_named):
    creat_camera = cmds.duplicate ('persp', smartTransform = True, name=cam_named)
    cmds.showHidden (creat_camera, a = True)
    return creat_camera #รีเทิร์นตัวแปรกล้องออกมา

#
def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

def cam_selected():
    selected_camera = cmds.ls(sl=True)
    cmds.select(d=True)
    return selected_camera

def new_imagePlane():
    imgPlane = cmds.imagePlane(n="imgRef")
    return imgPlane


def set_seq(obj):
    cmds.setAttr(obj + ".useFrameExtension", 1)


def setAttr_parent(b, a):
    cmds.parent(b, a)

def select_imp(imgPlane):
    a = cmds.fileDialog2(fileMode=1, caption="Select your Image")
    b = cmds.setAttr(imgPlane + ".imageName", a[0], type="string")
    
def size_manage(w, h, imgPlane):
    cmds.setAttr(imgPlane[0] + ".width", w/100)
    cmds.setAttr(imgPlane[0] + ".height", h/100)

def clear_tranImp(a):
    cmds.setAttr ("{}.translateX".format(a), 0)
    cmds.setAttr ("{}.translateY".format(a), 0)
    cmds.setAttr ("{}.translateZ".format(a), -20)
    cmds.setAttr ("{}.rotateX".format(a), 0)
    cmds.setAttr ("{}.rotateY".format(a), 0)
    cmds.setAttr ("{}.rotateZ".format(a), 0)
