from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z03TrolleyStarted import Z03TrolleyStarted


class Z02Initialized(BaseState):

    state = State.Initialized

    def run(self):
        print("Z02 - Initialized")

    def next(self, input):
        if input == Input.start_command_received:
            return Z03TrolleyStarted(self.communicator)

        return None