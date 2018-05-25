import threading
import time

from serial import Serial
import sys
from CommunicationServer.TrolleyCommunicationServer import TrolleyCommunicationServer
from States.Input import Input
from States.State import State
from States.Z01ControllerStarted import Z01ControllerStarted
from UartCommunication.UartObserver import UartObserver
from TrolleyController.TrolleyStateMachine import TrolleyStateMachine
from UartCommunication.UartOverUSBCommunicatorImplementation import UartOverUSBCommunicatorImplementation
from UartCommunication.CommunicationCommands import CommunicationCommands
from TrolleyController.ContactSwitchRecognizer import ContactSwitchRecognizer
from TrolleyController.ContactSwitchListener import ContactSwitchListener


class Main(threading.Thread, UartObserver, ContactSwitchListener):

    PORT = Serial("/dev/ttyACM0")

    stateMachine = None
    lock_stateMachine = threading.Lock()
    trolleyCommunicationServer = None
    controller_running = True
    contact_switch_triggered = False

    def __init__(self):
        threading.Thread.__init__(self)

        self._communicator = UartOverUSBCommunicatorImplementation(self.PORT)
        self._communicator.register_new_observer(self)

        self.stateMachine = TrolleyStateMachine(Z01ControllerStarted(self._communicator))

        self.trolleyCommunicationServer = TrolleyCommunicationServer(self)
        self.trolleyCommunicationServer.start()

        self._contact_switch_recognizer = ContactSwitchRecognizer(self)
        self._contact_switch_recognizer.start()

        self.stateMachine.next(Input.initialized)
        self.start()

    def run(self):

        while self.controller_running:
            if self.stateMachine.equals_state(State.TrolleyStopped):
                self.controller_running = False
                print("==================================")
                print("Exit")
                sys.exit(0)

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
        print(command, data)

        if command == CommunicationCommands.DESTINATION_REACHED:
            self.stateMachine.next(Input.destination_reached)
        elif command == CommunicationCommands.HEIGHT_REACHED:
            self.stateMachine.next(Input.clutch_destination_reached)


    def on_contact_switch_on(self):
        if not self.contact_switch_triggered:
            self.contact_switch_triggered = True
            print("Contact Switch")
            self.stateMachine.next(Input.stop_command_received)


if __name__ == "__main__":
    print("Starting Trolley")
    Main()