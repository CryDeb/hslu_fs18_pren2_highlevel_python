import signal
import sys
import time
from multiprocessing import Queue
from TargetRecognizer.TargetRecognizerMultithreadedPoolImpl import TargetRecognizerMultithreadedPoolImpl


def signal_handler(signal, frame):
    targetRecognize._stop_queue.put(True)
    print(queue.qsize())
    targetRecognize.stop_threads()
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
queue = Queue()
print("a")
targetRecognize = TargetRecognizerMultithreadedPoolImpl(queue=queue)
print("b")
#targetRecognize._read_image_infinite_loop(targetRecognize._stop_queue, queue)
targetRecognize.start_read_image_loop()
time.sleep(5)
targetRecognize.stop_threads()
print(queue.qsize())