import signal
from serial import Serial
import sys

from UartCommunicationCommandsTest import UartCommunicationCommandsTest


port = Serial("/dev/ttyACM1")
uart = UartCommunicationCommandsTest(port)
def signal_handler(signal, frame):
    uart.cleanup()
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    mode = int(input("Enter digit(1[drive distance], 2[stop], 3[send error]):"))
    if mode == 1:
        distance = int(input("Enter distance:"))
        uart.send_command1(distance)
    elif mode == 2:
        uart.send_command2()
    elif mode == 3:
        uart.send_command3()

