from abc import ABCMeta, abstractmethod


class ContactSwitchListener:
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_contact_switch_on(self): pass

