#The RP2040-YD modules features the Raspberry Pi RP2040 chip


The RP2040-YD modules features the Raspberry Pi RP2040 chip, and is pin compatible with the Raspberry Pi Pico board. It is assembled with the same, original RP2040 chip used on the original Raspberry Pi Pico board, but ads more Flash memory, USB Type C, LEDs and an additional button.PLEASE NOTE: The pin headers are yellow(as shown in photos) or red.This module carries the powerful Dual-core RP2040 processor with flexible clock running up to 133 MHz which is a low-power microcontrollers. It also has 264KB of SRAM, and 4MB Flash(W24Q32) memory.It is a high quality, high performance, low cost and easy to use module from VCC-GND Studio. We have been importing their products for a while now, and the assembly quality of their boards is very good.It makes 28 GPIO PINs of the RP2040 available via the two 20pin headers.A user button is available on the GP24 pin.The reset button is used to reset the system, or enter bootloader mode.It has a RGB WS2812 LED, a power LED and a blue user LED.
- Red LED: Used to indicate power on condition
- Blue User LED: On GP25, available to user
- RGB WS2812 LED: On GP23The RGB WS2812 LED is controlled by GP23, and has a Red, Green and Blue LED that are individually addressable. There are plenty of examples on the internet showing how to drive a WS2812 LED. For example, Google "WS2812 Arduino" or "WS2812 c code".Compared to the official Raspberry Pi Pico, this module has the following improvements:

    Added PWR power LED
    The USB interface was changed to type-C USB
    Added reset button to facilitate reset operation and firmware update operation
    Added a user button on GPIO24
    Added a RGB LED to GPIO23
    Increased FLASH memory from 2 to 4MB 


Specifications


    CPU Dual-core ARM Cortex M0+ processor up to 133MHz
    FLASH Memory 4MB off-chip
    SRAM 264KB
    Digital I/O Pins: 28
    Analog I/O Pins: 4
    I2C interface: 2
    SPI interface: 2
    UART interface: 2
    3 LEDs for power, user and programming
    User and Reset buttons
    USB Type-C connector
    Power supply and downloading interface USB Type-C
    Circuit Operating Voltage: 3.3V
    Supply Voltage via USB: 5V
    Power 3.3V/5V DC
    Dimensions 53.3 x 22.9mm 


Specs and Docs


    PDF Schematics
    Firmware, bootloader and micropython
    Micropython Example using the WS2812 LED
    Altium PCBDOC file 


Firmware Update

To update the firmware:

    First, connect the computer via a USB cable
    Press and hold the BOOT button
    Press the RST button
    Release the BOOT button after 1 second
    The computer will automatically recognize it as a removable hard disk
    Copy the firmware files to hard disk that appears and the core board will automatically reboot 


Package Includes

1 x RP2040 module
2 x 20 Pin Headers, 2.54mm Grid
1 x 4 Pin Headers, right angle, 2.54mm Grid