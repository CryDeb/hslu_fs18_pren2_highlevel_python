import signal
from serial import Serial

import sys


from TargetRecognizer.TargetRecognizerImp import TargetRecognizerImp
from UartCommunicationCommandsTest import UartCommunicationCommandsTest

port = Serial("/dev/ttyACM0")
uart = UartCommunicationCommandsTest(port)
port.timeout = 5
target = TargetRecognizerImp()
def signal_handler(signal, frame):
    uart.cleanup()
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    mode = int(input("Enter digit(1[drive distance], 2[stop], 3[send error]), 4[Claw to position], 5[close claw], 6[open claw]:"))
    if mode == 1:
        distance = int(input("Enter distance:"))
        print(distance)
        uart.send_command1(distance)
        print(port.read(1))
    elif mode == 2:
        uart.send_command2()
    elif mode == 3:
        uart.send_command3()
    elif mode == 4:
        distance = int(input("Enter position:"))
        print(distance)
        uart.send_command4(distance)
    elif mode == 5:
        uart.send_command5()
    elif mode == 6:
        uart.send_command6()
    elif mode == 7:
        uart.send_command1(250)
        #print(target.is_target_in_reach())
        while target.is_target_in_reach() != True:
            pass
        uart.emergency_stop()
        print("targetFound")
    elif mode == 8:
        uart.emergency_stop() 
