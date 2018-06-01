
class TrolleyStateMachine:

    currentState = None

    def __init__(self, initialState):
        self.currentState = initialState
        #self.currentState.run()

    def start(self):
        self.currentState.run()

    def equals_state(self, state):
        return self.currentState.get_state() == state

    def next(self, input, params=None):

        if input == None:
            print("XXX - State unchanged")
            return

        print(input)
        nextState = self.currentState.next(input)
        if nextState != None:
            self.currentState = nextState
            self.currentState.params = params
            self.currentState.run()