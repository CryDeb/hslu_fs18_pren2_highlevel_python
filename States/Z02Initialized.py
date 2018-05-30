from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z03TrolleyStarted import Z03TrolleyStarted


class Z02Initialized(BaseState):

    state = State.Initialized

    def run(self):
        print("Z02 - Initialized")

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator, self.uartObserver)
        elif input == Input.start_command_received:
            return Z03TrolleyStarted(self.communicator, self.uartObserver)

        return None