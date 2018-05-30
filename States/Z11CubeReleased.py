from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z12ClutchAscended import Z12ClutchAscended


class Z11CubeReleased(BaseState):

    state = State.CubeReleased

    def run(self):
        print("Z11 - Cube released")
        self.communicator.move_claw_to_top()

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator, self.uartObserver)
        elif input == Input.clutch_destination_reached:
            return Z12ClutchAscended(self.communicator, self.uartObserver)

        return None