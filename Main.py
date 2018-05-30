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


class Main(threading.Thread, UartObserver, ContactSwitchListener):

    PORT = Serial("/dev/ttyACM0")

    stateMachine = None
    lock_stateMachine = threading.Lock()
    trolleyCommunicationServer = None
    controller_running = True
    contact_switch_triggered = False
    target_recognized_triggered = False
    recognizer = None
    queue = None

    def __init__(self):
        threading.Thread.__init__(self)

        self._communicator = UartOverUSBCommunicatorImplementation(self.PORT)
        self._communicator.register_new_observer(self)

        self.stateMachine = TrolleyStateMachine(Z01ControllerStarted(self._communicator, self))

        self.trolleyCommunicationServer = TrolleyCommunicationServer(self)
        self.trolleyCommunicationServer.start()

        self._contact_switch_recognizer = ContactSwitchRecognizer(self)
        self._contact_switch_recognizer.start()


        self.queue = Queue()
        self.recognizer = TargetRecognizerMultithreadedPoolImpl(queue = self.queue)
        self.recognizer.start_read_image_loop()

        self.stateMachine.next(Input.initialized)
        self.start()

    def run(self):

        while self.controller_running:
            if self.stateMachine.equals_state(State.TrolleyStopped):
                self.controller_running = False
                print("==================================")
                print("Exit")
                sys.exit(0)

            if not self.queue.empty() and not self.target_recognized_triggered:
                self.target_recognized_triggered = True
                print("queue")
                print(self.queue.get())
                self.stateMachine.next(Input.target_recognized)

            time.sleep(0.1)


    def on_start_command(self):
        self.lock_stateMachine.acquire()
        try:
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

    def notify_about_arrived_notification(self, command, data):
        #print(command, data)
        #print(command, CommunicationCommands.VALUE.value, command == CommunicationCommands.VALUE.value)
        if command == CommunicationCommands.VALUE.value:
            pass
            #print("Value: " + str(data))

        if command == CommunicationCommands.DESTINATION_REACHED.value:
            self.stateMachine.next(Input.destination_reached)
        elif command == CommunicationCommands.HEIGHT_REACHED.value:
            self.stateMachine.next(Input.clutch_destination_reached)
        elif command == CommunicationCommands.CLOSE_CLAW.value:
            self.stateMachine.next(Input.cube_grabbed)
        elif command == CommunicationCommands.OPEN_CLAW.value:
            self.stateMachine.next(Input.cube_released)




    def on_contact_switch_on(self):
        if not self.contact_switch_triggered:
            self.contact_switch_triggered = True
            print("Contact Switch")
            self.stateMachine.next(Input.stop_command_received)


if __name__ == "__main__":
    print("Starting Trolley")
    Main()