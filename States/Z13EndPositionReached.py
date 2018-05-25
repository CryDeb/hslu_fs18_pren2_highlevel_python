from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped


class Z13EndPositionReached(BaseState):

    state = State.EndPositionReached

    def run(self):
        print("Z13 - End position reached")
        self.communicator.emergency_stop()

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator)

        return None