from numpy import mean, median
from numpy.ma import count

from OpenCVWrapper.OpenCV import OpenCV
import cv2


class TargetRecognizerImp:

    def __init__(self, open_cv=None):
        if isinstance(open_cv, OpenCV):
            self._open_cv = open_cv
        else:
            self._open_cv = OpenCV()

    def _target_recognize_algorithm(self, debug=False):
        if isinstance(self._open_cv, OpenCV):

            self._open_cv.capture_picture('/home/dane/Downloads/20180308_092236.mp4')
            self._open_cv.convert_to_black_and_white()

            if debug:
                #resize
                width, height = self._open_cv.get_image_dimension()
                self._open_cv.resize_image(None, height/1.2, width/1.2)

            #make black and white
            self._open_cv.calculate_level()
            image = self._open_cv.calculate_threshold()

            #countour calc
            self._open_cv.find_contours()
            approx_poly_dp = self._open_cv.get_all_approx_poly_dp()
            centerX = []
            centerY = []
            med = 0
            for approx_poly in approx_poly_dp:
                ma = self._open_cv.get_moments(image)
                image = self._open_cv.draw_contour(approx_poly)
                M = cv2.moments(approx_poly)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                centerX.append(cX)

                centerY.append(cY)
                #print("Center: " + str(M["m10"]) + " " + str(M["m00"]) + " " + str(M))
            meanX = median(centerX)
            meanY = median(centerY)
            finalX = []
            finalY = []
            for x in centerX:
                if meanX*0.85<x<meanX*1.15:
                    finalX.append(x)
            for y in centerY:
                if meanY*0.85<y<meanY*1.15:
                    finalY.append(y)
            if count(finalX) == count(finalY) >= 5:
                cv2.circle(image, (int(meanX), int(meanY)), 7, (120, 130, 120), -1)
                print("TargetRecognized")
            return image
        return None

    def is_target_in_reach(self):
        image = self._target_recognize_algorithm()
        if image is not None:
            self._open_cv.show_image(image)

    def calculate_distance_to_target(self):
        pass