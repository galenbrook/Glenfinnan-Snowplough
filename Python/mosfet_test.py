import RPi.GPIO as GPIO
import time

# Use Broadcom pin numbering
GPIO.setmode(GPIO.BCM)

# Set up GPIO 18 as an output pin
GPIO.setup(25, GPIO.OUT)

# Set GPIO 18 HIGH
while True:
    GPIO.output(25, GPIO.LOW)

# Optional: Keep it HIGH for 10 seconds
# while True:
#     time.sleep(2)

#GPIO.output(18, GPIO.LOW)

# Clean up GPIO settings
GPIO.cleanup()