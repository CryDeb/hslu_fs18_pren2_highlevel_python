import threading
import time
import RPi.GPIO as GPIO


class ContactSwitchRecognizer(threading.Thread):

    GPIO_PIN = 21
    _contact_switch_listener = None
    _last_state_on = False

    def __init__(self, contact_switch_listener):
        threading.Thread.__init__(self)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self._contact_switch_listener = contact_switch_listener

    def run(self):
        while True:
            input_state = GPIO.input(self.GPIO_PIN)
            if input_state == False and self._last_state_on == False:
                self._contact_switch_listener.on_contact_switch_on()

            self._last_state_on = not input_state

            time.sleep(0.05)
