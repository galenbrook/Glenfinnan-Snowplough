import time

from gpiozero import Button
from signal import pause

count = 0

def confirm_button_press():
    global count
    count+=1
    print("Button was pressed " + str(count) + " times!")

button = Button(pin=21, pull_up=False, bounce_time=0.01)

button.when_pressed = confirm_button_press

pause()