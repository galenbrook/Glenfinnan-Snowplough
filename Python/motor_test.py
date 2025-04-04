from gpiozero import PWMOutputDevice
from time import sleep

# Replace with the GPIO pin connected to your motor's control input (via transistor/MOSFET gate)
MOTOR_PWM_PIN = 18  # Example GPIO pin (supports hardware PWM)

# Set up the PWMOutputDevice
motor = PWMOutputDevice(MOTOR_PWM_PIN, frequency=1000, active_high=False)  # frequency in Hz
motor.value = 0.1

motor.pulse(fade_in_time=5, fade_out_time=5, background=False)

sleep(30)

print("Starting motor test...")
# 
# try:
#     # Ramp up speed
#     for speed in range(0, 101, 10):  # 0% to 100% in steps of 10%
#         motor.value = speed / 100
#         print(f"Motor speed: {speed}%")
#         sleep(5)
# 
#     # Hold at full speed
#     print("Running at full speed for 2 seconds...")
#     sleep(2)
# 
#     # Ramp down speed
#     for speed in range(100, -1, -10):  # 100% to 0% in steps of -10%
#         motor.value = speed / 100
#         print(f"Motor speed: {speed}%")
#         sleep(5)
# 
#     print("Test complete. Stopping motor.")

#finally:
#motor.off()  # Make sure motor is off when script ends