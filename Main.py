import threading
import time

from serial import Serial
import sys
from CommunicationServer.TrolleyCommunicationServer import TrolleyCommunicationServer
from States.Input import Input
from States.State import State
from multiprocessing import Queue
from States.Z01ControllerStarted import Z01ControllerStarted
from UartCommunication.UartObserver import UartObserver
from TrolleyController.TrolleyStateMachine import TrolleyStateMachine
from UartCommunication.UartOverUSBCommunicatorImplementation import UartOverUSBCommunicatorImplementation
from TrolleyController.ContactSwitchRecognizer import ContactSwitchRecognizer
from TrolleyController.ContactSwitchListener import ContactSwitchListener
from UartCommunication.CommunicationCommands import CommunicationCommands
from TargetRecognizer.TargetRecognizerMultithreadedPoolImpl import TargetRecognizerMultithreadedPoolImpl
from CommunicationServer.Log import Log


class Main(threading.Thread, UartObserver, ContactSwitchListener):

    PORT = Serial("/dev/ttyACM0")
    DISTANCE_BETWEEN_CAM_AND_CENTER = 18
    DISTANCE_BETWEEN_CHASSIS_AND_CLUTCH = 15
    DISTANCE_BETWEEN_CENTER_AND_START = 22

    MAGIC_CONSTANT = 1.6
    ASCENT = 0.14142135623731
    START_HEIGHT = 63.5

    TOF_FAILURE_THRESHOLD = 2
    SINA_DIV_SINB = 0.4663
    IMAGE_HALF_HEIGHT_IN_PIXEL = 480/2

    stateMachine = None
    lock_stateMachine = threading.Lock()
    trolleyCommunicationServer = None
    controller_running = True
    contact_switch_triggered = False
    target_recognized_triggered = False
    recognizer = None
    queue = None
    _communicator = None

    _got_first_init = False

    position_x = 0
    position_y = 70
    position_clutch = 0

    position_y_3_last = 70
    position_y_2_last = 70
    position_y_1_last = 70

    drive_distance_to_target = 0

    def __init__(self):
        threading.Thread.__init__(self)

        #TODO
        self._communicator = UartOverUSBCommunicatorImplementation(self.PORT)
        self._communicator.initialize_device()
        time.sleep(0.5)
        self._communicator.register_new_observer(self)


        self.trolleyCommunicationServer = TrolleyCommunicationServer(self)
        self.trolleyCommunicationServer.start()
        #return
        self._contact_switch_recognizer = ContactSwitchRecognizer(self)
        self._contact_switch_recognizer.start()

        self.queue = Queue()
        self.recognizer = TargetRecognizerMultithreadedPoolImpl(queue = self.queue)
        self.recognizer.start_read_image_loop()

        self.stateMachine = TrolleyStateMachine(Z01ControllerStarted(self._communicator, self))

        #self.trolleyCommunicationServer.log(Log(self.position_x, self.position_y, "log", self.getConvertedLogState()))
        #self.trolleyCommunicationServer.log(Log(self.position_x, self.position_y, "log", self.getConvertedLogState()))
        self.stateMachine.start()
        #self.stateMachine.next(Input.initialized)
        self.start()
        self.trolleyCommunicationServer.clear_logs()


    def run(self):

        while self.controller_running:
            if self.stateMachine.equals_state(State.TrolleyStopped):
                self.controller_running = False
                print("==================================")
                print("Exit")
                sys.exit(0)

            if not self.queue.empty() and not self.target_recognized_triggered:
                self.target_recognized_triggered = True
                #self.queue.queue.clear()
                #time.sleep(0.1)
                if not self.queue.empty():
                    #middle is 270
                    #print("queue")
                    queue_val = self.queue.get()
                    #print(queue_val)

                    print("y: " + str(self.position_y) + " * " + str(self.SINA_DIV_SINB) + " *("+str(queue_val[1]) +"-"+str(self.IMAGE_HALF_HEIGHT_IN_PIXEL)+")/" + str(self.IMAGE_HALF_HEIGHT_IN_PIXEL))
                    distance_to_cam = (self.position_y * self.SINA_DIV_SINB * (self.IMAGE_HALF_HEIGHT_IN_PIXEL-queue_val[1])) / self.IMAGE_HALF_HEIGHT_IN_PIXEL

                    self.drive_distance_to_target = int(self.DISTANCE_BETWEEN_CAM_AND_CENTER + distance_to_cam - 3)
                    if self.drive_distance_to_target < 0:
                        self.drive_distance_to_target = 0
                    print("DISTANCE: " + str(self.DISTANCE_BETWEEN_CAM_AND_CENTER) + " dis_to_cam: " + str(distance_to_cam) + " ")
                    print("Final drive distance: " + str(self.drive_distance_to_target))

                    #self._communicator.emergency_stop()
                    self.stateMachine.next(Input.target_recognized, self.drive_distance_to_target)

            time.sleep(0.1)


    def on_start_command(self):
        self.lock_stateMachine.acquire()
        try:
            self.trolleyCommunicationServer.clear_logs()
            self.stateMachine.next(Input.start_command_received)
        finally:
            self.lock_stateMachine.release()

        return None

    def on_stop_command(self):
        self.lock_stateMachine.acquire()
        try:
            self.stateMachine.next(Input.stop_command_received)
        finally:
            self.lock_stateMachine.release()

        return None

    def getConvertedLogState(self):
        if self.stateMachine == None:
            return Log.DEVICE_STOPPED
        elif self.stateMachine.equals_state(State.TrolleyStopped):
            return Log.DEVICE_STOPPED
        elif self.stateMachine.equals_state(State.ControllerStarted):
            return Log.DEVICE_STARTED
        elif self.stateMachine.equals_state(State.Initialized):
            return Log.DEVICE_STARTED
        elif self.stateMachine.equals_state(State.TrolleyStarted):
            return Log.DEVICE_STARTED
        elif self.stateMachine.equals_state(State.CubePositionReached):
            return Log.DEVICE_STARTED
        elif self.stateMachine.equals_state(State.ClutchDescended):
            return Log.DEVICE_STARTED
        elif self.stateMachine.equals_state(State.CubeGrabbed):
            return Log.PACKAGE_PICKED_UP
        elif self.stateMachine.equals_state(State.ClutchAscendedWithCube):
            return Log.OBSTACLE_PASSED
        elif self.stateMachine.equals_state(State.TargetRecognized):
            return Log.TARGET_DETECTED
        elif self.stateMachine.equals_state(State.TargetPositionReached):
            return Log.TARGET_DETECTED
        elif self.stateMachine.equals_state(State.ClutchDescendedWithCube):
            return Log.TARGET_DETECTED
        elif self.stateMachine.equals_state(State.CubeReleased):
            return Log.PACKAGE_DROPPED
        elif self.stateMachine.equals_state(State.ClutchAscended):
            return Log.PACKAGE_DROPPED
        elif self.stateMachine.equals_state(State.EndPositionReached):
            return Log.DESTINATION_REACHED


    def notify_about_arrived_notification(self, command, data):
        #print(command, data)
        #print(command, CommunicationCommands.VALUE.value, command == CommunicationCommands.VALUE.value)
        if command == CommunicationCommands.VALUE.value:
            #print("Value: " + str(data))
            value = (data[2] * 255 + data[1]) /10
            if data[0] == 2: # position x
                if value > 0:
                    self.position_x = self.DISTANCE_BETWEEN_CENTER_AND_START + (value * self.MAGIC_CONSTANT)
                    self.position_y = (self.position_x * self.ASCENT) + self.START_HEIGHT
            elif data[0] == 1: # position y (tof)
                print("Toff: "+str(value))
                if value > 0:
                    pre_median = sorted([self.position_y_1_last, self.position_y_2_last, self.position_y_3_last])[1]
                    #print("data2: " + str(data[2]) + " data1:" + str(data[1]))
                    #print("pre:" + str(pre_median) + " - tof:" + str(self.TOF_FAILURE_THRESHOLD) + " < " + str(value))
                    if pre_median-self.TOF_FAILURE_THRESHOLD < value and (pre_median-self.TOF_FAILURE_THRESHOLD)*2 > value :
                        self.position_y_3_last = self.position_y_2_last
                        self.position_y_2_last = self.position_y_1_last
                        self.position_y_1_last = value
                        # Median
                        self.position_y = sorted([self.position_y_1_last, self.position_y_2_last, self.position_y_3_last])[1]
                        #print("New Pos Y: " + str(self.position_y))
                        #print("pos_y:" + str(self.position_y) + " data:" + str(value))
                    elif (pre_median-self.TOF_FAILURE_THRESHOLD)*2 < value and value > 820:
                        #print("==== INIT TOF")
                        self._communicator.init_tof()

            elif data[0] == 3: # position y (claw)
                self.position_clutch = value

            if self.trolleyCommunicationServer != None:
                absolute_clutch_position = int(self.position_y - self.position_clutch - self.DISTANCE_BETWEEN_CHASSIS_AND_CLUTCH)
                #print("PosY:" + str(self.position_y) + " - PosC:" + str(self.position_clutch) + " - DISTANCE:" + str(self.DISTANCE_BETWEEN_CHASSIS_AND_CLUTCH) + " = Absolute:" + str(absolute_clutch_position))
                if absolute_clutch_position < 0:
                    absolute_clutch_position = 0
                self.trolleyCommunicationServer.log(Log(self.position_x, absolute_clutch_position, "log", self.getConvertedLogState()))

        if command == CommunicationCommands.DESTINATION_REACHED.value:
            #print("position_y: " + str(self.position_y) + " distance: " + str(self.DISTANCE_BETWEEN_CHASSIS_AND_CLUTCH))
            self.stateMachine.next(Input.destination_reached, int(self.position_y-self.DISTANCE_BETWEEN_CHASSIS_AND_CLUTCH))
        elif command == CommunicationCommands.HEIGHT_REACHED.value:
            self.stateMachine.next(Input.clutch_destination_reached)
        elif command == CommunicationCommands.CLOSE_CLAW.value:
            self.stateMachine.next(Input.cube_grabbed)
        elif command == CommunicationCommands.OPEN_CLAW.value:
            self.stateMachine.next(Input.cube_released)
        elif command == CommunicationCommands.INIT_DONE.value:
            self.stateMachine.next(Input.initialized)

    def on_contact_switch_on(self):
        if not self.contact_switch_triggered:
            #.contact_switch_triggered = True
            print("Contact Switch")
            self.stateMachine.next(Input.stop_command_received)
            #time.sleep()


if __name__ == "__main__":
    print("Starting Trolley")
    Main()
