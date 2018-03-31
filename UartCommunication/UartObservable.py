import abc
from UartCommunication.UartObserver import UartObserver


class UartObservable(abc.ABC):
    def __init__(self):
        print("yeah")
        self._observers = []

    def register_new_observer(self, observer):
        if isinstance(observer, UartObserver):
            self._observers.append(observer)

    def unregister_observer(self, observer):
        if isinstance(observer, UartObserver):
            self._observers.remove(observer)

    def notify_all_observers(self, command, data):
        for observer in self._observers:
            if isinstance(observer, UartObserver):
                observer.notify_about_arrived_notification(command, data)
