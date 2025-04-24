from display_driver import Display_Driver
from subprocess import Popen
from time import sleep

if __name__ == "__main__":
    sleep(10)
    display = Display_Driver()
    display.switch_off()
    Popen(["python", "/home/glenfinnan/snowplough/Glenfinnan-Snowplough/Python/main_driver.py"])
    