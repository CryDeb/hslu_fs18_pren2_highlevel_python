from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z09TargetPositionReached import Z09TargetPositionReached


class Z08TargetRecognized(BaseState):

    HORIZONTAL_DISTANCE_TO_TARGET = 10
    state = State.TargetRecognized

    def run(self):
        print("Z08 - Target recognized")
        self.communicator.drive_to_position(self.HORIZONTAL_DISTANCE_TO_TARGET)

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator)
        elif input == Input.destination_reached:
            return Z09TargetPositionReached(self.communicator)

        return None