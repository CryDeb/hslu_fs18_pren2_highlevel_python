from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z05ClutchDescended import Z05ClutchDescended


class Z04CubePositionReached(BaseState):

    VERTICAL_DISTANCE_TO_CUBE = 50
    state = State.CubePositionReached

    def run(self):
        print("Z04 - Cube position reached")
        self.communicator.move_claw_to_position(self.VERTICAL_DISTANCE_TO_CUBE)

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator)
        elif input == Input.clutch_destination_reached:
            return Z05ClutchDescended(self.communicator)

        return None