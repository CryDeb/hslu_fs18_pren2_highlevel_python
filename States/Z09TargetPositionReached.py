from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z10ClutchDescendedWithCube import Z10ClutchDescendedWithCube


class Z09TargetPositionReached(BaseState):

    VERTICAL_DISTANCE_TO_TARGET = 90
    state = State.TargetPositionReached

    def run(self):
        print("Z09 - Target position reached")
        if self.params != None:
            print("go to param: " + str(self.params))
            self.communicator.move_claw_to_position(self.params*1.2)
        else:
            print("go to else: " + str(self.VERTICAL_DISTANCE_TO_TARGET))
            self.communicator.move_claw_to_position(self.VERTICAL_DISTANCE_TO_TARGET)

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator, self.uartObserver)
        elif input == Input.clutch_destination_reached:
            return Z10ClutchDescendedWithCube(self.communicator, self.uartObserver)

        return None
