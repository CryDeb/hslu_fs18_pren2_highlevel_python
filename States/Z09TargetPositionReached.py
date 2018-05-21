from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z10ClutchDescendedWithCube import Z10ClutchDescendedWithCube


class Z09TargetPositionReached(BaseState):

    VERTICAL_DISTANCE_TO_TARGET = 10
    state = State.TargetPositionReached

    def run(self):
        print("Z09 - Target position reached")
        self.communicator.move_claw_to_position(self.VERTICAL_DISTANCE_TO_TARGET)

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator)
        elif input == Input.clutch_descended:
            return Z10ClutchDescendedWithCube(self.communicator)

        return None