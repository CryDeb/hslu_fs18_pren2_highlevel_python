from enum import Enum


class CommunicationCommands(Enum):
    ERROR = 0b00000000
    STOP_FOR_SPECIFIC_DISTANCE = 0b11100001
    DRIVE_FOR_SPECIFIC_DISTANCE = 0b10011001
    EMERGENCY_STOP = 0b01111000
    BACKWARDS_FOR_SPECIFIC_DISTANCE = 0b01010101
    MOVE_CLAW_TO_SPECIFIC_POSITION = 0b11001100
    MOVE_CLAW_TO_INITIAL_POSITION = 0b00101101
    OPEN_CLAW = 0b11010010
    CLOSE_CLAW = 0b00110011
    GET_VALUE = 0b01001011
    SET_VALUE = 0b10101010
    VALUE = 0b10000111
    ACKNOWLEGE = 0b01100110
    DESTINATION_REACHED = 0b00011110
    UNUSED_COMMAND01 = 0b11111111
    COMMAND_LENGTH = 8

    @classmethod
    def has_command(cls, value):
        return any(value == item.value for item in cls)

    @staticmethod
    def command_addition_length(value):
        if any(value == value == CommunicationCommands.STOP_FOR_SPECIFIC_DISTANCE, value == CommunicationCommands.DRIVE_FOR_SPECIFIC_DISTANCE,
               value == CommunicationCommands.BACKWARDS_FOR_SPECIFIC_DISTANCE, value == CommunicationCommands.MOVE_CLAW_TO_INITIAL_POSITION,
               value == CommunicationCommands.GET_VALUE, value == CommunicationCommands.ACKNOWLEGE):
            return 1
        elif any(value == CommunicationCommands.SET_VALUE, value == CommunicationCommands.VALUE):
            return 2
        else:
            return 0
