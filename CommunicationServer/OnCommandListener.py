from abc import ABCMeta, abstractmethod


class OnCommandListener:
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_start_command(self): pass

    @abstractmethod
    def on_stop_command(self): pass
