import abc


class UartObserver(abc.ABC):
    @abc.abstractmethod
    def notify_about_arrived_notification(self, command, data):
        pass