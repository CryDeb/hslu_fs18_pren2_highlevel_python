from TargetRecognizer.TargetRecognizerImp import TargetRecognizerImp
import cv2
from OpenCVWrapper.OpenCV import OpenCV

myTarget = TargetRecognizerImp()
myTarget.is_target_in_reach()
while(1):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#myTarget.is_target_in_reach()