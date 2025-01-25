# Video https://youtu.be/9w0BR8OFYNE
# Post http://kontakts.ru/showthread.php/40884?p=86175#post86175
# Обсуждения и поддержка: https://t.me/MrMicroPython
# Simulation On-Line https://wokwi.com/projects/421020239796862977

from MyServo import Servo
import time

# Initialize the servo on GPIO pin 16
servo = Servo(16)

# Set the servo to the initial position (0 degrees) and wait for 1 second
servo.ServoAngle(0)
time.sleep_ms(1000)

try:
    # Infinite loop to continuously sweep the servo back and forth
    while True:       
        # Sweep from 0 to 180 degrees
        for i in range(0, 180, 1):
            servo.ServoAngle(i)
            time.sleep_ms(15)
        
        # Sweep back from 180 to 0 degrees
        for i in range(180, 0, -1):
            servo.ServoAngle(i)
            time.sleep_ms(15)        
except Exception as e:
    # Catch all exceptions and ensure the servo is deinitialized safely
    print(f"An error occurred: {e}")
finally:
    # Ensure that resources are freed and the servo is turned off when done
    servo.deinit()
    print("Servo deinitialized.")

