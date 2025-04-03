import time
import psutil  # To check CPU usage
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory  # Optional: Use pigpio for better handling

# Use pigpio if available (better performance), otherwise use default
try:
    factory = PiGPIOFactory()
    button = Button(17, pin_factory=factory, bounce_time=0.2)  # Adjust bounce_time if needed
    print("Using pigpio backend.")
except Exception as e:
    button = Button(17, bounce_time=0.2)
    print("Using default RPi.GPIO backend.")

last_press_time = None

def button_pressed():
    global last_press_time
    now = time.time()
    
    # Calculate time since last press
    if last_press_time:
        time_since_last_press = now - last_press_time
    else:
        time_since_last_press = None
    
    last_press_time = now  # Update last press time
    
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=0)  # Get CPU usage without delay
    
    # Print diagnostic info
    print(f"[{time.strftime('%H:%M:%S')}] Button Pressed! "
          f"Time Since Last Press: {time_since_last_press:.3f}s, CPU: {cpu_usage}%")

def button_released():
    print(f"[{time.strftime('%H:%M:%S')}] Button Released!")

# Attach event handlers
button.when_pressed = button_pressed
button.when_released = button_released

print("Waiting for button presses. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    print("\nExiting...")
