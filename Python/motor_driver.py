import pigpio
import time

class Motor_Driver:
    """
    Controls a motor using software PWM on a Raspberry Pi via pigpio.

    This version uses pigpio's software PWM, which allows PWM on any GPIO pin.
    Multiple instances can be used for different pins. Duty cycle is internally
    tracked since pigpio software PWM does not expose current output state.
    """

    def __init__(self, gpio_pin=18, frequency=1000):
        self.gpio_pin = gpio_pin
        self.frequency = frequency
        self.current_speed = 0

        self.pi = pigpio.pi()
        if not self.pi.connected:
            raise IOError("Could not connect to pigpio daemon. Is 'pigpiod' running?")

        self.pi.set_PWM_frequency(self.gpio_pin, self.frequency)
        self.pi.set_PWM_dutycycle(self.gpio_pin, 0)

        print(f"Motor_Driver (software PWM via pigpio) initialized on GPIO {self.gpio_pin} at {self.frequency} Hz")

    def set_speed(self, duty_cycle_percent):
        """
        Immediately sets the motor speed.
        :param duty_cycle_percent: Speed as a percentage (0 to 100)
        """
        duty_cycle_percent = min(100, max(0, duty_cycle_percent))
        duty_cycle = int(duty_cycle_percent * 2.55)  # Convert to 0–255
        self.pi.set_PWM_dutycycle(self.gpio_pin, duty_cycle)
        self.current_speed = duty_cycle_percent
        print(f"[set_speed] Set speed to {duty_cycle_percent}%")

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

        for _ in range(steps):
            self.current_speed += delta
            duty_cycle = int(self.current_speed * 2.55)
            self.pi.set_PWM_dutycycle(self.gpio_pin, duty_cycle)
            time.sleep(step_delay)

        self.current_speed = target_speed
        final_duty = int(self.current_speed * 2.55)
        self.pi.set_PWM_dutycycle(self.gpio_pin, final_duty)
        print(f"[ramp_speed] Ramped to {target_speed}% over {ramp_time} seconds")

    def start_motor(self, target_speed=50, ramp_time=2.0):
        """
        Starts the motor and ramps to a safe startup speed.
        :param target_speed: Final speed (default 50%)
        :param ramp_time: Total ramp time in seconds
        """
        self.ramp_speed(target_speed, ramp_time)

    def stop(self):
        """Stops the motor and releases pigpio resources."""
        self.pi.set_PWM_dutycycle(self.gpio_pin, 0)
        self.pi.stop()
        self.current_speed = 0
        print("Motor stopped and pigpio resources released.")
        
    def run_lap(self):
        try:
            self.ramp_speed(60, ramp_time=3)
            time.sleep(13.5)
            self.ramp_speed(0, ramp_time=3)
        except Exception as exc:
            print("Exception occurred: " + exc)
        finally:
            self.ramp_speed(0, ramp_time=1)
        

# === Example Usage ===
if __name__ == "__main__":
    motor = Motor_Driver()
    motor.run_lap()