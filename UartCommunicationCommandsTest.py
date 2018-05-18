from UartCommunication.UartObserver import UartObserver
from UartCommunication.UartOverUSBCommunicatorImplementation import UartOverUSBCommunicatorImplementation

class UartCommunicationCommandsTest(UartObserver):

    def __init__(self, port):
        self._communicator = UartOverUSBCommunicatorImplementation(port)
        self._communicator.register_new_observer(self)

    def notify_about_arrived_notification(self, command, data):
        print(command, data)

    def send_command1(self, distance):
        self._communicator.drive_to_position(distance)

    def send_command2(self):
        self._communicator.stop_at_position(100)

    def send_command3(self):
        self._communicator.send_error()

    def send_command4(self, distance):
        self._communicator.move_claw_to_position(distance)

    def send_command5(self):
        self._communicator.close_claw()
	
    def send_command6(self):
        self._communicator.open_claw()

    def cleanup(self):
        self._communicator.clean_up()














