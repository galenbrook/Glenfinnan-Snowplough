from gpiozero import Button
from signal import pause
import RPi.GPIO as GPIO

class Button_Driver:
    def __init__(self, pin=12):
        self.button = Button(pin, pull_up=False, bounce_time=0.1)
        self._pressed_callback = None
        self._enabled = False
        print(f"Button successfully set up on pin {pin}.")

    def is_pressed(self):
        return self.button.is_pressed

    def when_pressed(self, callback):
        self._pressed_callback = callback
        if self._enabled:
            self.button.when_pressed = callback

    def enable(self):
        """Re-attach press callback to enable button input."""
        if self._pressed_callback:
            self.button.when_pressed = self._pressed_callback
        self._enabled = True

    def disable(self):
        """Detach press callback to disable button input."""
        self.button.when_pressed = None
        self._enabled = False

        
# Example usage


if __name__ == "__main__":
        
    def on_press(button_driver):
        print("Button pressed! Disabling input.")
        button_driver.disable()

    try:
        button = Button_Driver()
        button.when_pressed(lambda: on_press(button))  # Pass the instance to the callback
        button.enable()

        pause()
        
    except KeyboardInterrupt:
        print("Keyboard interrupt!")
    finally:
        GPIO.cleanup()
