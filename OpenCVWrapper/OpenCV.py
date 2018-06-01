import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

class OpenCV:

    def __init__(self):
        self._camera = None
        self._image = None
        self._contours = None
        self._min_size = 100
        self._max_size = 5500000
        #self._camera = PiCamera()
        #self._camera.resolution = (640, 480)
        #self._framerate = 15
        #self._rawCapture = PiRGBArray(self._camera, size=(640, 480))
        #time.sleep(0.1)

    def _get_image(self, image=None):
        if image is None:
            if self._image is None:
                if self.capture_picture() == -1:
                    return self._image
            return self._image
        return image

    def set_image(self, image):
        if image is not None:
            self._image = image

    def capture_picture(self, video_device=0):
        if self._camera is None:
            self._camera = cv2.VideoCapture(video_device)
        #if not (self._camera.isOpened()):
        #    return -1
            status, self._image = self._camera.read()
            if status:
                return self._image
        else:
            self._rawCapture = PiRGBArray(self._camera, size=(640, 480))
            self._camera.capture(self._rawCapture, format="bgr")
            self._image = self._rawCapture.array
            #self.save_image(image=self._image)
            return self._image
        return -1

    def get_image_dimension(self, image=None):
        image = self._get_image(image)
        if image is None:
            pass
        return image.shape[:2]

    def resize_image(self, image=None, new_height=None, new_width=None):
        image = self._get_image(image)
        if new_height is None:
            new_height, _ = self.get_image_dimension(image)
        if new_width is None:
            _, new_width = self.get_image_dimension(image)
        self._image = cv2.resize(image, (int(new_height), (int(new_width))))
        return self._image

    def convert_to_black_and_white(self, image=None):
        image = self._get_image(image)
        self._image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return self._image

    def calculate_threshold(self, image=None, threshold_value=60,  max_value=255, threshold_type=cv2.THRESH_BINARY):
        image = self._get_image(image)
        _, self._image = cv2.threshold(image, threshold_value, max_value, threshold_type)
        return self._image

    def calculate_level(self, image=None):
        image = self._get_image(image)
        #self._image = cv2.equalizeHist(image)
        return self._image

    def gaussian_blur(self, image=None):
        image = self._get_image(image)
        self._image = cv2.GaussianBlur(image, (5, 3), 0)
        return self._image

    def find_contours(self, image=None):
        image = self._get_image(image)
        _, self._contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return self._contours

    def get_approx_poly_dp(self, contour, min_size=None, max_size=None):
        if min_size is None:
            min_size = self._min_size
        if max_size is None:
            max_size = self._max_size
        peri = cv2.arcLength(contour, True)
        approx_poly_dp = cv2.approxPolyDP(contour, 0.04 * peri, True)
        if len(approx_poly_dp) == 4 and min_size < cv2.contourArea(contour) < max_size:
            return contour
        return -1

    def get_moments(self, image=None):
        image = self._get_image(image)
        return cv2.moments(image)

    def draw_contour(self, contour, image=None, contour_index=0, color=(135, 255, 0), thickness=2):
        image = self._get_image(image)
        cv2.drawContours(image, [contour], -1, (122, 255, 0), 2)
        return image

    def get_all_approx_poly_dp(self, contours=None):
        if contours is None:
            contours = self._contours
        approx_poly_dp = []
        for contour in contours:
            contour_to_store = self.get_approx_poly_dp(contour, self._min_size, self._max_size)
            if not isinstance(contour_to_store, int):
                approx_poly_dp.append(contour_to_store)
        return approx_poly_dp

    def show_image(self, image=None):
        image = self._get_image(image)
        cv2.imshow('Image', image)

    def moments(self, approx_poly):
        return cv2.moments(approx_poly)


    def save_image(self, destination="Test.jpg", image=None):
        cv2.imwrite(destination, image)