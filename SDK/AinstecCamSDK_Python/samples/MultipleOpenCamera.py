from time import sleep
from AinstecError import *
from Common import *
from Camera import *
from Util import *


def PrintCamInfoList():
    for i in range(len(camInfoList)):
        print("index", i, "is:", camInfoList[i].cameraIP, "ret:",
              camInfoList[i].errorCode, "cameraVersion:", camInfoList[i].cameraSystemVersion)


def OpenCamera():
    ret = cam.Open(camInfo)
    if ret == AC_OK:
        print("\033[1;32m", "Open",
            camInfo.cameraIP, "OK", "\033[0m")
    else:
        print("\033[1;31m" "Error. Can't Open",
            camInfo.cameraIP, "\033[0m")
        exit()
        
##### Start ####
cam = Camera().CreateCamera()

ret, camInfoList = cam.DiscoverCameras()
if ret != AC_OK:
    print("DiscoverCameras failed")
PrintCamInfoList()

defaultCameraIndex = 0
camInfo = camInfoList[defaultCameraIndex]
OpenCamera()
cam.Close(camInfo)

ret, camInfoList = cam.DiscoverCameras()
if ret != AC_OK:
    print("DiscoverCameras failed")
PrintCamInfoList()

defaultCameraIndex = 0
camInfo = camInfoList[defaultCameraIndex]
OpenCamera()

ret, exposure = cam.GetValue(camInfo, ParamType.IR_Exposure)
print("ret:", ret, "Get IR_Exposure:", exposure)

cam.Close(camInfo)

##### End ####
