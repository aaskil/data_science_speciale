# Capture.py

from Common import *
from AinstecError import *
from Camera import *
from Util import *


def PrintCamInfoList(camInfoList):
    for i in range(len(camInfoList)):
        print("index", i, "is:", camInfoList[i].cameraIP, "ret:",
              camInfoList[i].errorCode, "cameraVersion:", camInfoList[i].cameraSystemVersion)


def OpenOneCamera(cam, camInfoList, strWantedIP=None):
    for i in range(len(camInfoList)):
        if (strWantedIP is not None and camInfoList[i].cameraIP != strWantedIP):
            continue
        if cam.Open(camInfoList[i]) == AC_OK:
            print("\033[1;32m", "Open",
                  camInfoList[i].cameraIP, "OK", "\033[0m")
            return AC_OK, camInfoList[i]
    print("\033[1;31m" "Can't Open any camera.", "\033[0m")
    return AC_E_NO_CAMERA, CameraInfo()


def OutputAll(camInfo):
    camInfo.outputSettings.sendPoint3D = True
    camInfo.outputSettings.sendPointUV = True
    camInfo.outputSettings.sendTriangleIndices = True
    camInfo.outputSettings.sendDepthmap = True
    camInfo.outputSettings.sendNormals = True
    camInfo.outputSettings.sendPointColor = True
    camInfo.outputSettings.sendTexture = True
    camInfo.outputSettings.sendRemapTexture = True
    if camInfo.rgbStatus == AC_E_NOT_EXIST:
        camInfo.outputSettings.sendTexture = False


def SaveImages(camInfo, frameData):
    filePath = create_outdir()
    if frameData.textureSize:
        save_rgb(frameData.texture, camInfo.camParam, filePath)
    if frameData.depthmapSize:
        save_deepmap2tiff(frameData.depthmap, camInfo.camParam, filePath)
    if frameData.textureSize and frameData.pointUVSize:
        save_rgb_align_depth(frameData.texture, frameData.pointUV,
                             camInfo.camParam, filePath)
    if frameData.point3DSize and frameData.pointUVSize and frameData.triangleIndicesSize:
        save_point2wrl(frameData, filePath)
    if frameData.point3DSize:
        save_point2pcd(frameData, filePath)
    if frameData.depthmapSize:
        save_deepmap(frameData.depthmap, camInfo.camParam, filePath)
    if frameData.point3DSize and frameData.triangleIndicesSize:
        save_point2ply(frameData, filePath)
    if frameData.point3DSize and frameData.normalsSize:
        save_point2ply_normal_color(frameData, filePath)
    if frameData.remapTextureSize:
        save_ir(frameData.remapTexture, camInfo.camParam, filePath, True)


def main():
    cam = Camera().CreateCamera()  # Initializing cam inside main()

    ret, camInfoList = cam.DiscoverCameras()
    PrintCamInfoList(camInfoList)

    ret, camInfo = OpenOneCamera(cam, camInfoList)

    if ret == AC_OK:
        OutputAll(camInfo)
        frameData = FrameData()
        ret = cam.Capture(camInfo, frameData)
        if ret == AC_OK:
            SaveImages(camInfo, frameData)

        cam.Close(camInfo)


if __name__ == "__main__":
    main()
