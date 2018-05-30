from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z07ClutchAscendedWithCube import Z07ClutchAscendedWithCube


class Z06CubeGrabbed(BaseState):

    state = State.CubeGrabbed

    def run(self):
        print("Z06 - Cube grabbed")
        self.communicator.move_claw_to_top()

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator, self.uartObserver)
        elif input == Input.clutch_destination_reached:
            return Z07ClutchAscendedWithCube(self.communicator, self.uartObserver)

        return None