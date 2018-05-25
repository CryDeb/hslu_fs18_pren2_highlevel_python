from States.State import State
from States.BaseState import BaseState


class Z00TrolleyStopped(BaseState):

    state = State.TrolleyStopped

    def run(self):
        print("Z00 - Trolley stopped")
        self.communicator.emergency_stop()

    def next(self, input):
        assert 0, "There is nothing to do next. Restart device / programm."