from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z11CubeReleased import Z11CubeReleased
from UartCommunication.CommunicationCommands import CommunicationCommands
import time


class Z10ClutchDescendedWithCube(BaseState):

    state = State.ClutchDescendedWithCube

    def run(self):
        print("Z10 - Clutch descended with cube")
        self.communicator.open_claw()
        time.sleep(1)
        self.uartObserver.notify_about_arrived_notification(CommunicationCommands.OPEN_CLAW.value, [])

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator, self.uartObserver)
        elif input == Input.cube_released:
            return Z11CubeReleased(self.communicator, self.uartObserver)

        return None