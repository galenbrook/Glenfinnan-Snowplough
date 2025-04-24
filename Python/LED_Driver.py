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
    
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
    
#GPIO.cleanup()
        
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    led1 = LED_Driver(pin=19)
    led2 = LED_Driver(pin=20)
    led3 = LED_Driver(pin=12)
    led4 = LED_Driver(pin=22)
    led5 = LED_Driver(pin=23)
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    led5.on()
    print("LED turned on.")
    try:
        while True:
            time.sleep(1)
    except:
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.off()
    finally:
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.off()
        GPIO.cleanup()
        
    #time.sleep(60)
    #print("LED turned off")
#     led1.off()
#     led2.off()
#     led3.off()
#     led4.off()
#     led5.off()
#     GPIO.cleanup()