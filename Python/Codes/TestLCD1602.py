# Video https://youtu.be/vIH6wGJScnQ
# Post Сайт http://kontakts.ru/showthread.php/40884?p=86156#post86156
from machine import I2C, Pin
from i2c_lcd import I2cLcd
from utime import sleep

DEFAULT_I2C_ADDR = 0x27  # I2C address for LCD 1602 B
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)  # Initialize I2C bus
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)  # Initialize LCD (2 rows, 16 columns)

# Test 1: Check all pixels
def test_all_pixels():
    lcd.clear()
    lcd.putstr("Test 1: Pixels")
    sleep(1)
    
    # Turn on all pixels on the screen
    for row in range(2):  # 2 rows
        for col in range(16):  # 16 columns
            lcd.move_to(col, row)  # Move cursor
            lcd.putstr("*")  # Turn on pixel (display a star)
            sleep(0.1)  # Delay for visualization
    sleep(1)  # 1-second delay before clearing the screen

    # Chessboard pattern
    lcd.clear()
    for row in range(2):  # 2 rows
        for col in range(16):  # 16 columns
            if (row + col) % 2 == 0:  # Alternating chessboard pattern
                lcd.move_to(col, row)
                lcd.putstr("*")
            sleep(0.1)
    sleep(1)  # Delay after chessboard test
    lcd.clear()

# Test 2: Check ASCII table (only English characters)
def test_ascii_table():
    lcd.clear()
    lcd.putstr("Test 2: ASCII")
    sleep(1)
    
    for i in range(32, 127):  # Check visible ASCII characters (32 to 126)
        lcd.move_to(i % 16, i // 16)  # Move cursor
        lcd.putstr(chr(i))  # Display character
        sleep(0.1)  # Delay between characters
    sleep(1)  # Delay after the test
    lcd.clear()

# Test 3: Check custom characters (we will not use 'create_char', just show examples)
def test_custom_chars():
    lcd.clear()
    lcd.putstr("Test 3: Custom Chars")
    sleep(1)
    
    # Custom characters are not supported directly by this library,
    # so we will display basic examples (like drawing with stars)
    
    # Example: Draw a box-like shape using "*" characters
    for row in range(2):  # Rows
        for col in range(16):  # Columns
            if row == 0 or row == 1:  # Draw top and bottom border
                lcd.move_to(col, row)
                lcd.putstr("*")
            sleep(0.1)
    sleep(1)  # Pause before clearing the screen
    lcd.clear()

# Function to display a message
def display_message(message):
    lcd.clear()  # Clear screen before displaying message
    lcd.putstr(message)  # Display message

if __name__ == '__main__':
    # Run all tests sequentially
    display_message("Test 1")
    test_all_pixels()  # Run Test 1
    display_message("Test 2")
    test_ascii_table()  # Run Test 2
    display_message("Test 3")
    test_custom_chars()  # Run Test 3
    display_message("Done!")  # Final message
    sleep(2)  # Show "Done!" message for 2 seconds before clearing
    lcd.clear()  # Clear screen
    
