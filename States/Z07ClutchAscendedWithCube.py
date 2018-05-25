from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z08TargetRecognized import Z08TargetRecognized


class Z07ClutchAscendedWithCube(BaseState):

    state = State.ClutchAscendedWithCube

    def run(self):
        print("Z07 - Clutch ascended with cube")
        self.communicator.drive_forward(50)

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator)
        elif input == Input.target_recognized:
            return Z08TargetRecognized(self.communicator)

        return None