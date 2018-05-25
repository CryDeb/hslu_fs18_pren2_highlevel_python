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
            self._serialPort = serialPort
            self._run_deamon = True
            self._thread_daemon = None
            self._create_incoming_message_listener_thread()
        else:
            raise ReferenceError("the passed argument is no instance of serial class")

    def drive_to_position(self, drive_distance_in_mm):
        self._serialPort.write(bytes([0b10011001]))
        self._serialPort.write(bytes([drive_distance_in_mm]))

    def drive_forward(self):
        self.drive_to_position(255)

    def stop_at_position(self, distance_until_stopped_in_mm):
        self._serialPort.write(self._to_byte(CommunicationCommands.STOP_FOR_SPECIFIC_DISTANCE))
        self._serialPort.write(self._to_byte(distance_until_stopped_in_mm))

    def emergency_stop(self):
        self._serialPort.write([0b01111000])

    def close_claw(self):
        self._serialPort.write(bytes([0b00110011]))

    def open_claw(self):
        self._serialPort.write(bytes([0b11010010]))

    def move_claw_to_position(self, distance_to_trolley_in_mm):
        self._serialPort.write(bytes([0b11001100]))
        self._serialPort.write(bytes([distance_to_trolley_in_mm]))

    def move_claw_to_top(self):
        self._serialPort.write(bytes([0b11001100]))
        self._serialPort.write(bytes([0]))

    def send_error(self):
        self._serialPort.write(self._to_byte(CommunicationCommands.ERROR))

    def _serial_incoming_message_listener(self):
        while self._run_deamon:
            if isinstance(self._serialPort, Serial):
                incoming_command = self._from_byte(self._serialPort.read(1))
                if CommunicationCommands.has_command(incoming_command):
                    nmr_of_data = CommunicationCommands.command_addition_length(incoming_command)
                    data = []
                    for i in range(0, nmr_of_data):
                        data.append(self._from_byte(self._serialPort.read(1)))
                    self.notify_all_observers(incoming_command, data)
                else:
                    self.send_error()

    def _create_incoming_message_listener_thread(self):
        self._thread_daemon = Thread(self._serial_incoming_message_listener)
        self._thread_daemon.daemon = True
        self._thread_daemon.start()

    def clean_up(self):
        if self._thread_daemon != None:
            self._run_deamon = False
            self._thread_daemon.join()

    def _to_byte(self, number_to_parse):
        if isinstance(number_to_parse, int):
            return number_to_parse.to_bytes(1, 'big')
        else:
            return (0).to_bytes(1, 'big')

    def _from_byte(self, bytes_to_parse):
        return int.from_bytes(bytes_to_parse, 'big')
