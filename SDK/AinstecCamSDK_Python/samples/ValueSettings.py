from AinstecError import *
from Common import *
from Camera import *
from Util import *


def PrintParamMemu():
    count = 0
    print("\033[1;34m%-28s : %s" % ("[ParamType]", "[index]"), "\033[0m")
    for (param, index) in zip(ParamType.__members__, ParamType):
        print("%-28s : %d" % (param, int(index)), end="\t")
        count += 1
        if  count % 3 == 0:
            print("")
    if not count % 3 == 0:
        print("")


def PrintCamInfoList():
    for i in range(len(camInfoList)):
        print("index", i, "is:", camInfoList[i].cameraIP, "ret:",
              camInfoList[i].errorCode, "cameraVersion:", camInfoList[i].cameraSystemVersion)


def OpenOneCamera(strWantedIP=None):
    for i in range(len(camInfoList)):
        if (strWantedIP != None and camInfoList[i].cameraIP != strWantedIP):
            continue
        if(cam.Open(camInfoList[i]) == AC_OK):
            print("\033[1;32m", "Open",
                  camInfoList[i].cameraIP, "OK", "\033[0m")
            return AC_OK, camInfoList[i]
    print("\033[1;31m" "Can't Open any camera.", "\033[0m")
    return AC_E_NO_CAMERA, CameraInfo()


##### Start ####
cam = Camera().CreateCamera()

ret, camInfoList = cam.DiscoverCameras()
PrintCamInfoList()

ret, camInfo = OpenOneCamera()

if ret == AC_OK:
    exposure = 15
    ret = cam.SetValue(camInfo, ParamType.IR_Exposure, exposure)
    if ret != AC_OK:
        exit(ret)

    ret, exposure = cam.GetValue(camInfo, ParamType.IR_Exposure)
    if ret != AC_OK:
        exit(ret)
    print("Get IR_Exposure:", exposure)
    
    fillHole = 0
    ret = cam.SetValue(camInfo, ParamType.Algo_FillHole, fillHole)
    if ret != AC_OK:
        exit(ret)

    ret, fillHole = cam.GetValue(camInfo, ParamType.Algo_FillHole)
    if ret != AC_OK:
        exit(ret)
    print("Get Algo_FillHole:", fillHole)
    
    ret = cam.SetValue(camInfo, ParamType.Algo_Smooth, True)
    if ret != AC_OK:
        exit(ret)

    smoothType = 4  # 4: Z-median smoothing
    ret = cam.SetValue(camInfo, ParamType.Algo_SmoothType, smoothType)
    if ret != AC_OK:
        exit(ret)
    
    ret, smoothTypeInCamera = cam.GetValue(camInfo, ParamType.Algo_SmoothType)
    if ret != AC_OK:
        exit(ret)
    print("Get Algo_SmoothType:", smoothTypeInCamera)
    
    
if ret == AC_OK:
    while True:
        PrintParamMemu()
        print("Usage: set [index] [xxx]; get [index]; 'q' to exit")
        cmd = input("Please input your operation(e.g. set 258 1 or get 258): ")
        values = cmd.split()
        if cmd.find("q") != -1:
            break
        elif cmd.find("set") != -1:
            if len(values) < 3:
                print("Input error!")
            else:
                ret = cam.SetValue(camInfo, int(values[1]), float(values[2]))
                if ret == AC_OK:
                    print("\033[1;32m", "Set", ParamType(
                        int(values[1])), "OK", "\033[0m")
                else:
                    print("\033[1;31m", "Error. errocode:", ret, "\033[0m")
        elif cmd.find("get") != -1:
            if len(values) < 2:
                print("Input error!")
            else:
                ret, value = cam.GetValue(camInfo, int(values[1]))
                if ret == AC_OK:
                    print("\033[1;32m", "Get", ParamType(
                        int(values[1])), ":", value, "\033[0m")
                else:
                    print("\033[1;31m", "Error. errocode:", ret, "\033[0m")
        else:
            print("Input error!")
    
    cam.Close(camInfo)

##### End ####
