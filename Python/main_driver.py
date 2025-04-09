from LED_Driver import LED_Driver
from button_driver import Button_Driver
from motor_driver import Motor_Driver
#from display_driver import Display_Driver
from signal import pause
import RPi.GPIO as GPIO
import time


class Exhibition_Driver():
    def __init__(self):
                
        self.LED1 = LED_Driver(pin=16)
        self.LED2 = LED_Driver(pin=24)
        
        self.button = Button_Driver(pin=12)
        self.button.when_pressed(self.on_button_press)  # Pass the instance to the callback
        self.button.enable()
        
        print("Exhibition object successfully instantiated.")
        
        # self.motor1 = Motor_Driver(gpio_pin=18)
        # self.motor2 = Motor_Driver(gpio_pin=13)
        
        # self.display = Display_Driver()
    
    def wait_for_button(self):
        pause()
        
    def on_button_press(self):
        print("Button press detected. Disabling input.")
        self.button.disable()
        self.run_exhibition()

    def cleanup(self):
        print("Cleaning up GPIO pins.")
        self.LED1.LED_off()
        self.LED2.LED_off()
        GPIO.cleanup()
        
    def run_exhibition(self):
        self.LED1.LED_on()
        print("LED 1 on.")
        time.sleep(5)
        self.LED2.LED_on()
        print("LED 2 on.")
        time.sleep(5)
        self.LED2.LED_off()
        print("LED 2 off.")
        time.sleep(5)
        self.LED1.LED_off()
        print("LED 1 off.")
        time.sleep(2)
        
        print("Exhibition finished. Re-enabling button input.")
        self.button.enable()
        
        
def main():
    print("Starting up main exhibition program.")
    GPIO.setmode(GPIO.BCM)
    exhibition = Exhibition_Driver()
    
    try:
        print("Waiting for button press...")
        pause()
        
    except KeyboardInterrupt:
        print("Keyboard interrupt!")
        
    except:
        print("Unknown exception!")
    
    finally:
        exhibition.cleanup()
        
if __name__ == "__main__":
    main()

