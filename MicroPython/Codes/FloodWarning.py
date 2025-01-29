# Video https://youtu.be/P4ZkJdV1Law
# Post http://kontakts.ru/showthread.php/40884?p=86158#post86158
from machine import Pin, ADC, PWM, I2C
from i2c_lcd import I2cLcd    
from time import sleep

DEFAULT_I2C_ADDR = 0x27     # LCD 1602 I2C address
Raindrop_AO = ADC(0)        # ADC0 multiplexing pin is GP26 (for raindrop sensor)
Buzzer = 12                 # Passive Buzzer Pin Definition             
buzzer = PWM(Pin(Buzzer))   # Initializing PWM for the buzzer

# Define LED pins
led_red = Pin(4, Pin.OUT)     # Red LED pin (to indicate rain)
led_green = Pin(5, Pin.OUT)   # Green LED pin (to indicate no rain)

def setup():
    global lcd 
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)  # Initialize I2C communication
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)          # Initialize LCD screen

def loop():
    while True:
        text = 'Warning!\nFlood warning!'  # Message to be shown on the LCD
        adc_Raindrop = Raindrop_AO.read_u16()  # Read analog value from raindrop sensor

        # Check if the raindrop sensor value indicates rain (low value = rain detected)
        if adc_Raindrop < 30000:
            lcd.putstr(text)  # Display warning message on LCD
            
            # Turn on red LED and start blinking
            led_red.value(1)   # Red LED ON
            led_green.value(0) # Green LED OFF
            buzzer.duty_u16(1000)  # Activate buzzer
            buzzer.freq(294)        # Set buzzer frequency to 294Hz (a specific tone)
            sleep(0.5)              # Wait for half a second
            lcd.clear()             # Clear the LCD screen
            buzzer.freq(495)        # Set buzzer frequency to 495Hz (different tone)
            sleep(0.5)              # Wait for half a second
        else:
            # Turn on green LED and turn off red LED
            led_red.value(0)   # Red LED OFF
            led_green.value(1) # Green LED ON
            buzzer.duty_u16(0)  # Deactivate the buzzer

        sleep(1)  # Delay between sensor readings

if __name__ == '__main__':
    setup()  # Set up LCD and sensors
    loop()   # Start the main loop
