from machine import Pin, PWM
import time

class Servo(object):
    def __init__(self, pin: int = 15, hz: int = 50):
        """
        Initialize the Servo object.

        :param pin: GPIO pin number to which the servo is connected (default: 15)
        :param hz: PWM frequency (default: 50 Hz)
        """
        self._servo = PWM(Pin(pin))
        self._servo.freq(hz)
    
    def ServoDuty(self, duty: int):
        """
        Set the PWM duty cycle for the servo.

        :param duty: Duty cycle in the range [1638, 8190].
        :raises ValueError: If the duty is out of the valid range.
        """
        # Ensure the duty cycle is within the acceptable range
        if duty < 1638 or duty > 8190:
            raise ValueError("Duty must be between 1638 and 8190.")
        
        # Set the PWM duty cycle
        self._servo.duty_u16(duty)
        
    def ServoAngle(self, pos: int):
        """
        Set the angle of the servo.

        :param pos: The angle in degrees [0, 180].
        :raises ValueError: If the position is out of the valid range.
        """
        # Limit the angle to the range 0-180
        if pos < 0 or pos > 180:
            raise ValueError("Position must be between 0 and 180 degrees.")
        
        # Convert the angle to the corresponding PWM duty cycle
        pos_buffer = (pos / 180) * 6552
        self._servo.duty_u16(int(pos_buffer) + 1638)

    def ServoTime(self, us: int):
        """
        Set the servo position by pulse width in microseconds.

        :param us: Pulse width in microseconds [500, 2500].
        :raises ValueError: If the pulse width is out of the valid range.
        """
        # Limit the pulse width to the range 500-2500 microseconds
        if us < 500 or us > 2500:
            raise ValueError("Pulse width must be between 500 and 2500 microseconds.")
        
        # Convert the pulse width to the corresponding PWM duty cycle
        pos_buffer = (us / 1000) * 3276
        self._servo.duty_u16(int(pos_buffer))
        
    def deinit(self):
        """
        Deinitialize the PWM and free the resources.
        """
        self._servo.deinit()

    def smooth_move(self, start_angle: int, end_angle: int, step: int = 5, delay: float = 0.02):
        """
        Smoothly move the servo from start_angle to end_angle in small steps.

        :param start_angle: Starting angle in degrees [0, 180].
        :param end_angle: Ending angle in degrees [0, 180].
        :param step: The step size in degrees (default: 5).
        :param delay: Time to wait between steps in seconds (default: 0.02).
        """
        if start_angle < 0 or start_angle > 180 or end_angle < 0 or end_angle > 180:
            raise ValueError("Angles must be between 0 and 180 degrees.")
        
        # Determine the direction of the movement (increasing or decreasing)
        if start_angle < end_angle:
            step = abs(step)
        else:
            step = -abs(step)
        
        for angle in range(start_angle, end_angle, step):
            self.ServoAngle(angle)
            time.sleep(delay)
        
        # Ensure the final angle is set exactly
        self.ServoAngle(end_angle)

