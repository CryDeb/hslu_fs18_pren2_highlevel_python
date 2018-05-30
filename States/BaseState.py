class BaseState:

    state = None
    communicator = None
    uartObserver = None

    def __init__(self, communicator, uartObserver):
        self.communicator = communicator
        self.uartObserver = uartObserver

    def get_state(self):
        return self.state

    def run(self):
        print("BaseState run")

    def next(self, input):
        assert 0, "Not implemented."
