import sys
sys.path.append(r'C:\Users\Student\Documents\ASJO\SDK\MultiCast')
import time
import msvcrt
import MultiCast
sys.path.append(r'C:\Users\Student\Documents\ASJO\SDK\AinstecCamSDK_Python\samples')
import Capture


if __name__ == "__main__":
    MultiCast.main()  
    time.sleep(1)
    Capture.main()
