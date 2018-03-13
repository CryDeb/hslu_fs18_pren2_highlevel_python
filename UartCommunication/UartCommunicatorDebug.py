from UartCommunication.UartCommunicator import UartCommunicator
from UartCommunication.UartObservable import UartObservable


class UartCommunicatorDebug(UartObservable, UartCommunicator):
    def __init__(self):
        super()
        UartObservable.__init__(self)

    def drive_to_position(self, drive_distance_in_mm):
        print(str(drive_distance_in_mm))

    def drive_forward(self):
        pass

    def stop_at_position(self, distance_until_stopped_in_mm):
        pass

    def close_claw(self):
        pass

    def open_claw(self):
        pass

    def move_claw_to_position(self, distance_to_trolley_in_mm):
        pass

    def move_claw_to_top(self):
        pass