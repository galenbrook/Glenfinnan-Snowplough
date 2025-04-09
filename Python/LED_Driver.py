import RPi.GPIO as GPIO
import time

# Idea is to create a dictionary relating GPIO pin
# numbers to physical positions of lights in the exhibition
LED_pinlist = [23,22,12,20,19,4,27,21,13,26]

class LED_Driver():
    def __init__(self, pin):
        self.pin = pin
        #self.ledPosition = ledPosition
        #self.positionCode = {self.ledPosition, self.gpioPin}
        
        GPIO.setup(self.pin, GPIO.OUT)
        print(f"LED driver successfully set up on pin {pin}.")
    
    def LED_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        
    def LED_off(self):
        GPIO.output(self.pin, GPIO.LOW)
    
#GPIO.cleanup()
        
if __name__ == "__main__":
    led1 = LED_Driver(pin=16)
    led2 = LED_Driver(pin=24)
    led1.LED_on()
    led2.LED_on()
    print("LED turned on.")
    time.sleep(30)
    print("LED turned off")
    led1.LED_off()
    led2.LED_off()
    GPIO.cleanup()