from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z04CubePositionReached import Z04CubePositionReached


class Z03TrolleyStarted(BaseState):

    HORIZONTAL_DISTANCE_TO_CUBE = 37
    state = State.TrolleyStarted

    def run(self):
        print("Z03 - Trolley started")
        self.communicator.drive_to_position(self.HORIZONTAL_DISTANCE_TO_CUBE)

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator, self.uartObserver)
        elif input == Input.destination_reached:
            return Z04CubePositionReached(self.communicator, self.uartObserver)

        return None