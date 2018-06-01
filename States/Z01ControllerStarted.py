from States.BaseState import BaseState
from States.Input import Input
from States.State import State
from States.Z00TrolleyStopped import Z00TrolleyStopped
from States.Z02Initialized import Z02Initialized
import time

class Z01ControllerStarted(BaseState):

    state = State.ControllerStarted
    _drive_initialized = False

    def run(self):
        print("Z01 - Controller started")
        #self.communicator.initialize_device()
        #time.sleep(0.2)
        self.communicator.init_pull_up_claw()

    def next(self, input):
        if input == Input.stop_command_received:
        	print("stop claw/drive")
        	self.communicator.emergency_stop()

        	if self._drive_initialized == False:
        		self._drive_initialized = True
        		print("init drive")
        		time.sleep(3)
        		self.communicator.init_drive_back()
        		print("initing drive")
        	else:
        		print("initialize device")
        		self.communicator.initialize_device()
        		print("initialize done")

        elif input == Input.initialized:
        	self.communicator.initialize_device()
        	time.sleep(0.2)
        	return Z02Initialized(self.communicator, self.uartObserver)

        return None