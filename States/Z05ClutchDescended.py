from States.BaseState import BaseState
from States.State import State
from States.Input import Input
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z06CubeGrabbed import Z06CubeGrabbed
from UartCommunication.CommunicationCommands import CommunicationCommands
import time

class Z05ClutchDescended(BaseState):

    state = State.ClutchDescended

    def run(self):
        print("Z05 - Clutch descended")
        self.communicator.close_claw()
        time.sleep(0.5)
        self.uartObserver.notify_about_arrived_notification(CommunicationCommands.CLOSE_CLAW.value, [])

    def next(self, input):
        if input == Input.stop_command_received:
            return Z00TrolleyStopped(self.communicator, self.uartObserver)
        elif input == Input.cube_grabbed:
            return Z06CubeGrabbed(self.communicator, self.uartObserver)

        return None