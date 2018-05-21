import json
import copy


class LogJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Log):
            return super(LogJSONEncoder, self).default(obj)

        dictionary = copy.deepcopy(obj.__dict__)
        dictionary["state"] = obj.get_state_name()
        return dictionary


class Log:
    DEVICE_STOPPED = -1
    DEVICE_STARTED = 0
    PACKAGE_PICKED_UP = 1
    OBSTACLE_PASSED = 2
    TARGET_DETECTED = 3
    PACKAGE_DROPPED = 4
    DESTINATION_REACHED = 5

    __state_list = {
        -1: "DEVICE_STOPPED",
        0: "DEVICE_STARTED",
        1: "PACKAGE_PICKED_UP",
        2: "OBSTACLE_PASSED",
        3: "TARGET_DETECTED",
        4: "PACKAGE_DROPPED",
        5: "DESTINATION_REACHED"
    }

    x = 0
    y = 0
    message = 0
    state = -1

    def __init__(self, x, y, message, state):
        self.x = x
        self.y = y
        self.message = message
        self.state = state

    def get_state_name(self):
        return self.__state_list.get(self.state)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return json.dumps(self, separators=(',', ':'), cls=LogJSONEncoder)
