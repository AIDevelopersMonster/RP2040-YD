# Video https://youtu.be/Bx2hbwIr0JY
# Post http://kontakts.ru/showthread.php/40884?p=86211#post86211
# Telega https://t.me/MrMicroPython
# 📜 Лицензия 🔗 Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
# 📂 Оригинальный код для платы PicoMate https://wiki.deskpi.com/picomate/#pinout-diagram
import time 
import board 
import busio
from adafruit_sht31d import SHT31D

i2c1 = busio.I2C(scl = board.GP15, sda = board.GP14) 

# Temperature & Humidity Sensor
sht_sensor = SHT31D(i2c1)

loopcount = 0

while True:
    print("\nTemperature: %0.1f C" % sht_sensor.temperature) 
    print("Humidity: %0.1f %%" % sht_sensor.relative_humidity) 
    loopcount += 1
    time.sleep(2)

    # every 10 passes turn on the heater for 1 second
    if loopcount == 10: 
        loopcount = 0 
        sht_sensor.heater = True
        print("Sensor Heater status =", sht_sensor.heater) 
        time.sleep(1)
        sht_sensor.heater = False
        print("Sensor Heater status =", sht_sensor.heater)
