from serial import Serial, SerialException
from UartCommunication.UartOverUSBCommunicatorImplementation import UartOverUSBCommunicatorImplementation


class UartCommunicationCreator:
    @staticmethod
    def create_uart_communicator(path_to_device):
        if isinstance(path_to_device, str):
            try:
                port = Serial(path_to_device)
                return UartOverUSBCommunicatorImplementation(port)
            except SerialException:
                return None
