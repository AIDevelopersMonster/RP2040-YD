# Video https://youtu.be/eqQt_BPlnCk
# Post http://kontakts.ru/showthread.php/40884?p=86150#post86150
from machine import Pin, I2C

# Инициализация I2C с назначением пинов вручную (для I2C0)
i2c = I2C(0, sda=Pin(0), scl=Pin(1))

# Сканирование устройств на шине I2C
devices = i2c.scan()
if devices:
    print("Devices found:", devices)
else:
    print("No I2C devices found")
