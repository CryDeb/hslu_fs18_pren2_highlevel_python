from enum import Enum


class State(Enum):
    TrolleyStopped = 0
    ControllerStarted = 1
    Initialized = 2
    TrolleyStarted = 3
    CubePositionReached = 4
    ClutchDescended = 5
    CubeGrabbed = 6
    ClutchAscendedWithCube = 7
    TargetRecognized = 8
    TargetPositionReached = 9
    ClutchDescendedWithCube = 10
    CubeReleased = 11
    ClutchAscended = 12
    EndPositionReached = 13
