import pigpio
import time

class Motor_Driver:
    """
    Controls a motor using hardware PWM on a Raspberry Pi via pigpio.

    Supports one motor per instance. Multiple instances can be used to control
    multiple motors, as long as each uses a GPIO pin on a separate PWM channel:
      - PWM0: GPIO 12 or 18
      - PWM1: GPIO 13 or 19
    """

    def __init__(self, gpio_pin=18, frequency=1000):
        self.gpio_pin = gpio_pin
        self.frequency = frequency
        self.pi = pigpio.pi()
        self.current_speed = 0  # Keep track of current duty % internally

        if not self.pi.connected:
            raise IOError("Could not connect to pigpio daemon. Is 'pigpiod' running?")

        self.pi.set_mode(self.gpio_pin, pigpio.OUTPUT) # Ensure pin is set as output
        
        print(f"Motor_Driver initialized on GPIO {self.gpio_pin} with {self.frequency} Hz PWM")

    def set_speed(self, target_speed):
        """
        Immediately steps the motor speed.
        Generally would not be recommended to use this but instead use ramp_speed.
        This will avoid large inrush currents or back EMF that could damage the circuitry
        (although there are protections in place that are supposed to stop this).
        Should be fine if e.g you need to emergency stop.
        :param target_speed: Speed as a percentage (0 to 100)
        """
        target_speed = min(100, max(0, target_speed))
        duty_cycle = int(target_speed * 10000)  # Convert to 0-1,000,000
        self.pi.hardware_PWM(self.gpio_pin, self.frequency, duty_cycle)
        self.current_speed = target_speed
        print(f"[set_speed] Set speed to {target_speed}%")

    def ramp_speed(self, target_speed, ramp_time=1.0):
        """
        Gradually ramps motor speed from current speed to target speed.
        :param target_speed: Target speed as percentage (0–100)
        :param ramp_time: Time in seconds to complete the ramp
        """
        target_speed = min(100, max(0, target_speed))
        steps = 25
        step_delay = ramp_time / steps
        delta = (target_speed - self.current_speed) / steps

        for i in range(steps):
            self.current_speed += delta
            duty_cycle = int(self.current_speed * 10000)
            self.pi.hardware_PWM(self.gpio_pin, self.frequency, duty_cycle)
            time.sleep(step_delay)

        # Ensure final value is exact
        self.current_speed = target_speed
        final_duty = int(self.current_speed * 10000)
        self.pi.hardware_PWM(self.gpio_pin, self.frequency, final_duty)
        print(f"[ramp_speed] Ramped to {target_speed}% over {ramp_time} seconds")

    def start_motor(self, target_speed=50, ramp_time=2.0):
        """
        Starts the motor and ramps to a safe startup speed.
        :param target_speed: Final speed (default 50%)
        :param ramp_time: Total ramp time in seconds
        """
        self.ramp_speed(target_speed, ramp_time)

    def stop(self):
        """Stops the motor and releases the pigpio resource."""
        self.pi.hardware_PWM(self.gpio_pin, 0, 0)
        self.pi.stop()
        self.current_speed = 0
        print("Motor stopped and pigpio resources released.")


if __name__ == "__main__":
#     motor_a = Motor_Driver(gpio_pin=18)
#     motor_b = Motor_Driver(gpio_pin=13)
# 
#     try:
#         motor_a.start_motor(target_speed=40)
#         motor_b.start_motor(target_speed=60)
#         time.sleep(3)
#         motor_a.set_speed(70)
#         motor_b.set_speed(30)
#         time.sleep(2)
#     finally:
#         motor_a.stop()
#         motor_b.stop()

    motor = Motor_Driver()

    try:
        motor.start_motor(target_speed=50)
        #time.sleep(5)
        motor.ramp_speed(50, ramp_time=5)
        time.sleep(10)
        motor.ramp_speed(20, ramp_time=5)
    finally:
        motor.stop()