from gpiozero import Button, LED
from signal import pause

count = 0

def confirm_button_press():
    global count
    count+=1
    print("Button was pressed " + str(count) + " times!")
    if (count%2):
        led.on()
    else:
        led.off()


button = Button(pin=18, pull_up=True, bounce_time=0.005)
led = LED(pin=20)

button.when_pressed = confirm_button_press

pause()