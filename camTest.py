from TargetRecognizer.TargetRecognizerMultithreadedPoolImpl import TargetRecognizerMultithreadedPoolImpl
from multiprocessing import Queue
import time

queue = Queue()
recognizer = TargetRecognizerMultithreadedPoolImpl(queue = queue)
recognizer.start_read_image_loop()

while True:
	time.sleep(0.05)
	if not queue.empty():
		print("Something in the queue")
		print(str(queue.get()))		