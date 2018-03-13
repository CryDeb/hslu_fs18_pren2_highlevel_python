from UartCommunication.CommunicationCommands import CommunicationCommands
from UartCommunication.UartCommunicator import UartCommunicator
from UartCommunication.UartObservable import UartObservable
from serial import Serial
from threading import Thread


class UartOverUSBCommunicatorImplementation(UartCommunicator, UartObservable):
    def __init__(self, serialPort):
        super()
        UartObservable.__init__(self)
        if isinstance(serialPort, Serial):
            self.__serialPort = serialPort
            self.__notification
        else:
            raise ReferenceError("the passed argument is no instance of serial class")

    def drive_to_position(self, drive_distance_in_mm):
        self.__serialPort.write(self.__to_byte(CommunicationCommands.DRIVE_FOR_SPECIFIC_DISTANCE))
        self.__serialPort.write(self.__to_byte(drive_distance_in_mm))

    def drive_forward(self):
        self.drive_to_position(0)

    def stop_at_position(self, distance_until_stopped_in_mm):
        self.__serialPort.write(self.__to_byte(CommunicationCommands.OPEN_CLAW))
        self.__serialPort.write(self.__to_byte(distance_until_stopped_in_mm))

    def close_claw(self):
        self.__serialPort.write(self.__to_byte(CommunicationCommands.CLOSE_CLAW))
        pass

    def open_claw(self):
        self.__serialPort.write(self.__to_byte(CommunicationCommands.OPEN_CLAW))

    def move_claw_to_position(self, distance_to_trolley_in_mm):
        self.__serialPort.write(self.__to_byte(CommunicationCommands.MOVE_CLAW_TO_SPECIFIC_POSITION))
        self.__serialPort.write(self.__to_byte(distance_to_trolley_in_mm))

    def move_claw_to_top(self):
        self.__serialPort.write(self.__to_byte(CommunicationCommands.MOVE_CLAW_TO_INITIAL_POSITION))

    def send_error(self):
        self.__serialPort.write(self.__to_byte(CommunicationCommands.ERROR))

    def __serial_incoming_message_listener(self):
        while True:
            if isinstance(self.__serialPort, Serial):
                incoming_command = self.__from_byte(self.__serialPost.read(1))
                if CommunicationCommands.has_command(incoming_command):
                    nmr_of_data = CommunicationCommands.command_addition_length(incoming_command)
                    data = None
                    if nmr_of_data == 1:
                        data = self.__from_byte(self.__serialPort.read(1))
                    elif nmr_of_data == 2:
                        data = self.__from_byte(self.__serialPort.read(2))
                    self.notify_all_observers(incoming_command, data)
                else:
                    self.send_error()

    def __create_incoming_message_listener_thread(self):
        thread_daemon = Thread(self.__serial_incomming_mesage_listener())
        thread_daemon.daemon = True
        thread_daemon.start()

    def __to_byte(self, number_to_parse):
        return number_to_parse.to_bytes(1, 'big')

    def __from_byte(self, bytes_to_parse):
        return int.from_bytes(bytes_to_parse, 'big')
