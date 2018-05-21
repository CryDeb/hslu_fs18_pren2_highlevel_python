from CommunicationServer.OnCommandListener import OnCommandListener
from CommunicationServer.TrolleyCommunicationServer import TrolleyCommunicationServer
from CommunicationServer.Log import Log
import time
import threading

class TrolleyControllerDummy(threading.Thread, OnCommandListener):

    trolleyCommunicationServer = None
    lock_state = threading.Lock()
    stateRunning = False

    SLEEP_TIME_IN_SECONDS = 0.1

    positionX = 150
    positionY = 360
    current_state = Log.DEVICE_STOPPED

    def __init__(self):
        threading.Thread.__init__(self)
        print("Init TrolleyControllerDummy")

        self.trolleyCommunicationServer = TrolleyCommunicationServer(self)
        self.trolleyCommunicationServer.start()
        self.start()

        self.trolleyCommunicationServer.log(Log(self.positionX, self.positionY, "IDLE", self.current_state))
        #self.trolleyCommunicationServer.log(Log(1, 1, "going", Log.DEVICE_STARTED))
        #self.trolleyCommunicationServer.log(Log(2, 5, "Packet", Log.PACKAGE_PICKED_UP))
        #self.trolleyCommunicationServer.log(Log(2, 2, "Abort", Log.DEVICE_STOPPED))

    def run(self):
        print("running")
        self.trolleyCommunicationServer.log(Log(self.positionX, self.positionY, "going", self.current_state))
        self.current_state = Log.DEVICE_STARTED
        self.trolleyCommunicationServer.log(Log(self.positionX, self.positionY, "going", self.current_state))
        while True:
            if self.stateRunning:


                self.trolleyCommunicationServer.log(Log(self.positionX, self.positionY, "going", self.current_state))

                if self.positionY > 250 and self.positionX < 160:
                    print("1")
                    self.positionY -= 2
                    self.current_state = Log.PACKAGE_PICKED_UP
                elif self.positionX >= 400 and self.positionY < 360:
                    print("2")
                    self.positionY += 2
                elif self.positionX > 300 and self.positionX < 350:
                    print("3")
                    self.current_state = Log.OBSTACLE_PASSED
                    self.positionX += 2
                    self.positionY -= 0.5
                elif self.positionX >= 350 and self.positionX < 400:
                    print("4")
                    self.current_state = Log.TARGET_DETECTED
                    self.positionX += 2
                    self.positionY -= 0.5
                elif self.positionX < 400:
                    print("5")
                    self.positionX += 2
                    self.positionY -= 0.5
                elif self.positionX >= 400 and self.positionY >= 360:
                    print("6")
                    self.current_state = Log.PACKAGE_DROPPED
                    #self.positionX += 2
                    #x§self.positionY -= 0.5


                print("move to " + str(self.positionX) + "," + str(self.positionY))
                time.sleep(self.SLEEP_TIME_IN_SECONDS)

    def on_start_command(self):
        print("Start Trolley")
        self.lock_state.acquire()
        try:
            self.stateRunning = True
        finally:
            self.lock_state.release()

        return None

    def on_stop_command(self):
        print("Stop Trolley")

        self.lock_state.acquire()
        try:
            self.stateRunning = False
            self.trolleyCommunicationServer.log(Log(self.positionX, self.positionY, "Abort", Log.DEVICE_STOPPED))
        finally:
            self.lock_state.release()

        return None
        # return "Failure: couldn't stop the trolley!"


if __name__ == "__main__":
    print("Starting Controller")
    TrolleyControllerDummy()