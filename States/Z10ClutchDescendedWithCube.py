from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z11CubeReleased import Z11CubeReleased


class Z10ClutchDescendedWithCube(BaseState):

    state = State.ClutchDescendedWithCube

    def run(self):
        print("Z10 - Clutch descended with cube")
        self.communicator.open_claw()

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator)
        elif input == Input.cube_released:
            return Z11CubeReleased(self.communicator)

        return None