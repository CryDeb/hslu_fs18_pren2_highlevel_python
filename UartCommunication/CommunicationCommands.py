from enum import Enum


class CommunicationCommands(Enum):
    ERROR = 0b11111111
    STOP_FOR_SPECIFIC_DISTANCE = 0b11100001
    DRIVE_FOR_SPECIFIC_DISTANCE = 0b10011001
    EMERGENCY_STOP = 0b01111000
    HEIGHT_REACHED = 0b01010101
    MOVE_CLAW_TO_SPECIFIC_POSITION = 0b11001100
    MOVE_CLAW_TO_INITIAL_POSITION = 0b00101101
    OPEN_CLAW = 0b11010010
    CLOSE_CLAW = 0b00110011
    GET_VALUE = 0b01001011
    SET_VALUE = 0b10101010
    VALUE = 0b10000111
    UNUSED = 0b01100110
    DESTINATION_REACHED = 0b00011110
    COMMAND_LENGTH = 8

    @classmethod
    def has_command(cls, value):
        return any(value == item.value for item in cls)

    @staticmethod
    def command_addition_length(value):
        if value == CommunicationCommands.STOP_FOR_SPECIFIC_DISTANCE.value or value == CommunicationCommands.DRIVE_FOR_SPECIFIC_DISTANCE.value or \
               value == CommunicationCommands.HEIGHT_REACHED.value or value == CommunicationCommands.MOVE_CLAW_TO_INITIAL_POSITION.value or \
               value == CommunicationCommands.GET_VALUE.value or value == CommunicationCommands.UNUSED.value:
            return 1
        elif value == CommunicationCommands.SET_VALUE.value or value == CommunicationCommands.VALUE.value:
            return 2
        else:
            return 0
