from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z13EndPositionReached import Z13EndPositionReached


class Z12ClutchAscended(BaseState):

    state = State.ClutchAscended

    def run(self):
        print("Z12 - Clutch ascended")
        self.communicator.drive_forward()

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator)
        elif input == Input.contact_switch_triggered:
            return Z13EndPositionReached(self.communicator)

        return None