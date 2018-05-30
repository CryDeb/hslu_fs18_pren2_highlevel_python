import threading
from itertools import count
from multiprocessing import Queue
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import sleep
from numpy import median
from picamera.array import PiRGBArray
from picamera import PiCamera



from OpenCVWrapper.OpenCV import OpenCV


class TargetRecognizerMultithreadedPoolImpl:

    def __init__(self, number_of_workers=15, queue = Queue()):
        self._workers = number_of_workers
        self._observers = []
        self._open_cv = OpenCV()
        self._position_x_y_queue = queue
        self._stop_queue = Queue()
        self._read_image = self._get_image
        self._read_image_thread = None
        #self._read_image = self._get_image_py

    def register(self, observer):
        self._observers.append(observer)

    def start_infinite_loop(self):
        while True:
            self._open_cv

    def _target_recognize_algorithm(self, open_cv, image, queue):
        open_cv.set_image(image)
        open_cv.convert_to_black_and_white()
        open_cv.calculate_threshold()
        open_cv.find_contours()
        approx_poly_dp = open_cv.get_all_approx_poly_dp()
        center_x = []
        center_y = []
        for approx_poly in approx_poly_dp:
            moments = open_cv.moments(approx_poly)
            center_x.append(int(moments["m10"] / moments["m00"]))
            center_y.append(int(moments["m01"] / moments["m00"]))
        if center_x:
            mean_x = median(center_x)
            mean_y = median(center_y)
            final_xy = []
            for x, y in zip(center_x, center_y):
                if mean_x * 0.80 < x < mean_x * 1.3 and mean_y * 0.80 < y < mean_y * 1.3:
                    final_xy.append((x, y))
            if len(final_xy) >= 5:
                x, y = zip(*final_xy)
                queue.put((median(x), median(y)))
                return

    def _get_image(self):
        return self._open_cv.capture_picture()

    def _get_image_py(self):
        pass

    def _read_image_infinite_loop(self, stop_queue, pos_x_y_queue):
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
        executor_pool = ThreadPoolExecutor(max_workers=25)
        sleep(1)
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            executor_pool.submit(self._target_recognize_algorithm, OpenCV(), image, pos_x_y_queue)
            rawCapture.truncate(0)
            if not stop_queue.empty():
                break
        camera.close()
        executor_pool.shutdown(5)

    def start_read_image_loop(self):
        self._read_image_thread = threading.Thread(target=self._read_image_infinite_loop, args=(self._stop_queue, self._position_x_y_queue))
        self._read_image_thread.start()

    def stop_threads(self):
        self._stop_queue.put(True)
        if isinstance(self._read_image_thread, threading.Thread):
            self._read_image_thread.join()

