from States.BaseState import BaseState
from States.Input import Input
from States.State import State
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z02Initialized import Z02Initialized


class Z01ControllerStarted(BaseState):

    state = State.ControllerStarted

    def run(self):
        print("Z01 - Controller started")

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator)
        elif input == Input.initialized:
            return Z02Initialized(self.communicator)

        return None