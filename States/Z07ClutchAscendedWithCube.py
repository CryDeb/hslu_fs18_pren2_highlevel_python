from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z08TargetRecognized import Z08TargetRecognized


class Z07ClutchAscendedWithCube(BaseState):

    state = State.ClutchAscendedWithCube

    def run(self):
        print("Z07 - Clutch ascended with cube")
        self.communicator.drive_to_position(255)

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator, self.uartObserver)
        elif input == Input.target_recognized:
            return Z08TargetRecognized(self.communicator, self.uartObserver)

        return None