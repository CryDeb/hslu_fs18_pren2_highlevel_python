from OpenCVWrapper.OpenCV import OpenCV
import cv2


class TargetRecognizerImp:

    def __init__(self, open_cv=None):
        if isinstance(open_cv, OpenCV):
            self._open_cv = open_cv
        else:
            self._open_cv = OpenCV()

    def _target_recognize_algorithm(self):
        if isinstance(self._open_cv, OpenCV):

            self._open_cv.capture_picture('/home/dane/Downloads/20180308_092329.jpg')
            self._open_cv.convert_to_black_and_white()

            #resize
            width, height = self._open_cv.get_image_dimension()
            self._open_cv.resize_image(None, height/3, width/3)

            #make black and white
            self._open_cv.calculate_level()
            image = self._open_cv.calculate_threshold()

            #countour calc
            self._open_cv.find_contours()
            approx_poly_dp = self._open_cv.get_all_approx_poly_dp()
            for approx_poly in approx_poly_dp:
                ma = self._open_cv.get_moments(image)
                image = self._open_cv.draw_contour(approx_poly)
                M = cv2.moments(approx_poly)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                print("Center: " + str(M["m10"] / M["m00"]))
            return image
        return None

    def is_target_in_reach(self):
        image = self._target_recognize_algorithm()
        if image is not None:
            self._open_cv.show_image(image)
