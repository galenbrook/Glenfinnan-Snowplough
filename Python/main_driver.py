from LED_Driver import LED_Driver
from button_driver import Button_Driver
from motor_driver import Motor_Driver
from display_driver import Display_Driver
from signal import pause
from multiprocessing import Process
import RPi.GPIO as GPIO
import time

finalVideoPath = "/home/glenfinnan/snowplough/Glenfinnan-Snowplough/Media/Snowplough_video.mp4"
testVideoPath = "/home/glenfinnan/snowplough/Glenfinnan-Snowplough/Media/test_video.mp4"

class Exhibition_Driver():
    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)
        self.LED1 = LED_Driver(pin=19)
        self.LED2 = LED_Driver(pin=20)
        self.LED3 = LED_Driver(pin=12)
        self.LED4 = LED_Driver(pin=22)
        self.LED5 = LED_Driver(pin=23)
        
        
        self.button = Button_Driver(pin=16)
        #self.button.when_pressed(self.on_button_press)  # Pass the instance to the callback
        #self.button.enable()
                
        self.motor1 = Motor_Driver(gpio_pin=18)
        # self.motor2 = Motor_Driver(gpio_pin=13)
        
        self.display = Display_Driver(videoPath=finalVideoPath)
        
        print("Exhibition object successfully instantiated.")
    
    def wait_for_button(self):
        pause()
        
    def on_button_press(self):
        print("Button press detected. Disabling input.")
        self.button.disable()
        self.run_exhibition()

    def cleanup(self):
        print("Cleaning up GPIO pins.")
#         self.LED1.off()
#         self.LED2.off()
        self.motor1.ramp_speed(0, ramp_time=1)
        self.motor1.stop()
        GPIO.cleanup()
        
    def run_lights(self):
        time.sleep(4)
        # Timestamp 0:30
        time.sleep(30)
        self.LED5.on()
        # Timestamp 0:44
        time.sleep(10)
        self.LED5.off()
        self.LED4.on()
        # Timestamp 0:56
        time.sleep(12)
        self.LED4.off()
        self.LED1.on()
        # Timestamp 1:33
        time.sleep(37)
        self.LED1.off()
        self.LED2.on()
        # Timestamp 1:45
        time.sleep(12)
        self.LED2.off()
        # Timestamp 3:15
        time.sleep(90)
        self.LED1.on()
        self.LED2.on()
        self.LED3.on()
        self.LED4.on()
        self.LED5.on()
        # Timestamp 3:45
        time.sleep(30)
        self.LED1.off()
        self.LED2.off()
        self.LED3.off()
        self.LED4.off()
        self.LED5.off()
    
    def run_display(self):
        self.display.toggle_standby()
        self.display.play_video()
        time.sleep(199)
        self.display.toggle_standby()
    
    def run_motor(self):
        self.motor1.run_lap()
        time.sleep(199)
        self.motor1.run_lap()
        self.motor1.stop()
    
    def run_exhibition(self, useButton=True):
        
        if (useButton):
            print("Waiting for button press...")
            self.button.wait_for_press()
            print("Button pressed.")
            
        print("Starting exhibition cycle...")
     
       ## Whatever we want the exhibition to actually do goes here ##
         
        displayProc = Process(target=self.run_display)
        motorProc = Process(target=self.run_motor)
        
        time.sleep(1)
        motorProc.start()
        
        time.sleep(19)
        displayProc.start()
        
        # Timestamp 0:04
        time.sleep(4)
        self.LED3.on()
        # Timestamp 0:30
        time.sleep(30)
        self.LED3.off()
        self.LED5.on()
        # Timestamp 0:44
        time.sleep(10)
        self.LED5.off()
        self.LED4.on()
        # Timestamp 0:56
        time.sleep(12)
        self.LED4.off()
        self.LED1.on()
        # Timestamp 1:33
        time.sleep(37)
        self.LED1.off()
        self.LED2.on()
        # Timestamp 1:45
        time.sleep(12)
        self.LED2.off()
        # Timestamp 3:15
        time.sleep(90)
        self.LED1.on()
        self.LED2.on()
        self.LED3.on()
        self.LED4.on()
        self.LED5.on()
        # Timestamp 3:45
        time.sleep(30)
        self.LED1.off()
        self.LED2.off()
        self.LED3.off()
        self.LED4.off()
        self.LED5.off()
        
        
        displayProc.join()
        motorProc.join()
        
        ## End of exhibition cycle code ##
        
        print("Exhibition cycle finished.")
        
        if (useButton):
            print("Re-enabling button input.")
        # self.button.enable()
        
        
def main():
    print("Starting up main exhibition program.")
    GPIO.setmode(GPIO.BCM)
    exhibition = Exhibition_Driver()
    useButton = True
    
    if(useButton):
        try:
            while True:
                exhibition.run_exhibition(useButton=True)
                            
        except KeyboardInterrupt:
            print("Keyboard interrupt!")
            
        except Exception as exc:
            print("An exception occurred!", exc)
        
        finally:
            exhibition.cleanup()
            
    else:
        try:
            exhibition.run_exhibition(useButton=False)
                            
        except KeyboardInterrupt:
            print("Keyboard interrupt!")
            
        except Exception as exc:
            print("An exception occurred!", exc)
        
        finally:
            exhibition.cleanup()

        
if __name__ == "__main__":
    main()


