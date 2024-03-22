# Importing necessary libraries
import sys
import threading
import msvcrt
import numpy as np
import cv2
import os
from ctypes import *
import time

# Importing MvCameraControl_class
sys.path.append("../MvImport")
from MvCameraControl_class import *

g_bExit = False

# Function to handle image capturing for each camera
def work_thread(cam, save_dir):
    stOutFrame = MV_FRAME_OUT()  
    memset(byref(stOutFrame), 0, sizeof(stOutFrame))
    
    # Capture a single image
    ret = cam.MV_CC_GetImageBuffer(stOutFrame, 5000)
    if None != stOutFrame.pBufAddr and 0 == ret:
        print ("get one frame: Width[%d], Height[%d], nFrameNum[%d]"  % (stOutFrame.stFrameInfo.nWidth, stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nFrameNum))
            
        # Convert the raw buffer to a numpy array
        img_data = np.array(stOutFrame.pBufAddr[:stOutFrame.stFrameInfo.nFrameLen], dtype=np.uint8)
        img_data = img_data.reshape((stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nWidth))
            
        # Convert to BGR format for OpenCV
        img_bgr = cv2.cvtColor(img_data, cv2.COLOR_BayerBG2BGR)
            
        # Save the image with a unique name
        image_name = f"image_{stOutFrame.stFrameInfo.nFrameNum}.jpg"
        image_path = os.path.join(save_dir, image_name)

        # Check if the file already exists
        if os.path.exists(image_path):
            # If the file exists, find a unique name by appending a suffix
            count = 1
            while True:
                new_image_name = f"image_{stOutFrame.stFrameInfo.nFrameNum}_{count}.jpg"
                new_image_path = os.path.join(save_dir, new_image_name)
                if not os.path.exists(new_image_path):
                    # Found a unique name
                    image_path = new_image_path
                    break
                count += 1

        # Save the image
        cv2.imwrite(image_path, img_bgr)
        print(f"Image saved to: {image_path}")
            
        nRet = cam.MV_CC_FreeImageBuffer(stOutFrame)
    else:
        print ("no data[0x%x]" % ret)


def main():
    # Enumerate devices
    deviceList = MV_CC_DEVICE_INFO_LIST()
    tlayerType = MV_GIGE_DEVICE
    ret = MvCamera.MV_CC_EnumDevices(tlayerType, deviceList)
    if ret != 0:
        print ("enum devices fail! ret[0x%x]" % ret)
        sys.exit()

    if deviceList.nDeviceNum == 0:
        print ("find no device!")
        sys.exit()

    print ("find %d devices!" % deviceList.nDeviceNum)

    # Select the first device
    nConnectionNum = 0

    # Create camera instances
    cam1 = MvCamera()
    cam2 = MvCamera()

    # Select device and create handle for the first camera
    stDeviceList1 = cast(deviceList.pDeviceInfo[nConnectionNum], POINTER(MV_CC_DEVICE_INFO)).contents
    ret = cam1.MV_CC_CreateHandle(stDeviceList1)
    if ret != 0:
        print ("create handle fail! ret[0x%x]" % ret)
        sys.exit()

    # Select device and create handle for the second camera
    stDeviceList2 = cast(deviceList.pDeviceInfo[nConnectionNum+1], POINTER(MV_CC_DEVICE_INFO)).contents
    ret = cam2.MV_CC_CreateHandle(stDeviceList2)
    if ret != 0:
        print ("create handle fail! ret[0x%x]" % ret)
        sys.exit()

    # Open devices
    ret = cam1.MV_CC_OpenDevice(MV_ACCESS_Control, 0)
    if ret != 0:
        print ("open device fail! ret[0x%x]" % ret)
        sys.exit()

    ret = cam2.MV_CC_OpenDevice(MV_ACCESS_Control, 0)
    if ret != 0:
        print ("open device fail! ret[0x%x]" % ret)
        sys.exit()

    # Start grabbing images for both cameras
    ret = cam1.MV_CC_StartGrabbing()
    if ret != 0:
        print ("start grabbing fail! ret[0x%x]" % ret)
        sys.exit()

    ret = cam2.MV_CC_StartGrabbing()
    if ret != 0:
        print ("start grabbing fail! ret[0x%x]" % ret)
        sys.exit()

    # Create threads for each camera
    save_dir1 = r'C:\Users\Student\Documents\ASJO\SDK\data\multicast\camera1'
    save_dir2 = r'C:\Users\Student\Documents\ASJO\SDK\data\multicast\camera2'
    
    try:
        hThreadHandle1 = threading.Thread(target=work_thread, args=(cam1, save_dir1))
        hThreadHandle2 = threading.Thread(target=work_thread, args=(cam2, save_dir2))
        time.sleep(4.20)
        hThreadHandle1.start()
        hThreadHandle2.start()
    except:
        print ("error: unable to start thread")
        
    print ("press a key to stop grabbing.")
    msvcrt.getch()

    g_bExit = True
    hThreadHandle1.join()
    hThreadHandle2.join()

    # Stop grabbing images for both cameras
    ret = cam1.MV_CC_StopGrabbing()
    if ret != 0:
        print ("stop grabbing fail! ret[0x%x]" % ret)
        sys.exit()

    ret = cam2.MV_CC_StopGrabbing()
    if ret != 0:
        print ("stop grabbing fail! ret[0x%x]" % ret)
        sys.exit()

    # Close devices
    ret = cam1.MV_CC_CloseDevice()
    if ret != 0:
        print ("close deivce fail! ret[0x%x]" % ret)
        sys.exit()

    ret = cam2.MV_CC_CloseDevice()
    if ret != 0:
        print ("close deivce fail! ret[0x%x]" % ret)
        sys.exit()

    # Destroy handles
    ret = cam1.MV_CC_DestroyHandle()
    if ret != 0:
        print ("destroy handle fail! ret[0x%x]" % ret)
        sys.exit()

    ret = cam2.MV_CC_DestroyHandle()
    if ret != 0:
        print ("destroy handle fail! ret[0x%x]" % ret)
        sys.exit()
if __name__ == "__main__":
    main()

