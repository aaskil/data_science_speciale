from AinstecError import *
from Common import *
from Camera import *
from Util import *


def PrintCamInfoList():
    for i in range(len(camInfoList)):
        print("index", i, "is:", camInfoList[i].cameraIP, "ret:",
              camInfoList[i].errorCode, "cameraVersion:", camInfoList[i].cameraSystemVersion)


def OpenAllCamera():
    for camInfo in camInfoList:
        ret = cam.Open(camInfo)
        if ret == AC_OK:
            print("\033[1;32m", "Open",
                  camInfo.cameraIP, "OK", "\033[0m")
        else:
            print("\033[1;31m" "Can't Open",
                  camInfo.cameraIP, "\033[0m")
            return ret
    return AC_OK


##### Start ####
cam = Camera().CreateCamera()

ret, camInfoList = cam.DiscoverCameras()
PrintCamInfoList()

ret = OpenAllCamera()

if ret == AC_OK:
    for camInfo in camInfoList:
        if cam.CameraGetVersion(camInfo) == AC_OK:
            print("cameraSystemVersion:\t", camInfo.cameraSystemVersion)
            print("ainstecCamSdkVersion:\t", camInfo.ainstecCamSdkVersion)

for camInfo in camInfoList:
    cam.Close(camInfo)

##### End ####
