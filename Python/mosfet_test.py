import RPi.GPIO as GPIO
import time

# Use Broadcom pin numbering
GPIO.setmode(GPIO.BCM)

# Set up GPIO 18 as an output pin
GPIO.setup(18, GPIO.OUT)

# Set GPIO 18 HIGH
GPIO.output(18, GPIO.HIGH)

# Optional: Keep it HIGH for 10 seconds
# while True:
#     time.sleep(2)

#GPIO.output(18, GPIO.LOW)

# Clean up GPIO settings
GPIO.cleanup()