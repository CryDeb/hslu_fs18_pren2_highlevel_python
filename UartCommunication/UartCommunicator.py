import abc

class UartCommunicator(abc.ABC):
    @abc.abstractmethod
    def drive_to_position(self, drive_distance_in_mm):
        pass

    @abc.abstractmethod
    def drive_forward(self):
        pass

    @abc.abstractmethod
    def stop_at_position(self, distance_until_stopped_in_mm):
        pass

    @abc.abstractmethod
    def close_claw(self):
        pass

    @abc.abstractmethod
    def open_claw(self):
        pass

    @abc.abstractmethod
    def move_claw_to_position(self, distance_to_trolley_in_mm):
        pass

    @abc.abstractmethod
    def move_claw_to_top(self):
        pass

    @abc.abstractmethod
    def init_pull_up_claw(self):
        pass

