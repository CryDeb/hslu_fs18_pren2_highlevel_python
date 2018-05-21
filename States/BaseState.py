class BaseState:

    state = None
    communicator = None

    def __init__(self, communicator):
        self.communicator = communicator

    def get_state(self):
        return self.state

    def run(self):
        print("BaseState run")

    def next(self, input):
        assert 0, "Not implemented."
