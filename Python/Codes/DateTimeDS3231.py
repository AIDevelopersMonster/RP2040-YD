# Video https://youtu.be/v333leLF_rc
# Post http://kontakts.ru/showthread.php/40884?p=86151#post86151
# Video как установить врпемя https://youtu.be/WD6t7rocsAE
# Код и тема "Как установить время " тут http://kontakts.ru/showthread.php/40889
from machine import Pin, I2C
import time

# Инициализация I2C с назначением пинов
i2c = I2C(0, sda=Pin(0), scl=Pin(1))

# Адрес DS3231
address = 0x68

# Функция для преобразования BCD в десятичное число
def bcd_to_dec(bcd):
    return (bcd & 0x0F) + ((bcd >> 4) * 10)

# Чтение времени с DS3231
def read_time():
    data = i2c.readfrom_mem(address, 0x00, 7)  # Чтение 7 байтов данных
    second = bcd_to_dec(data[0] & 0x7F)
    minute = bcd_to_dec(data[1] & 0x7F)
    hour = bcd_to_dec(data[2] & 0x3F)
    day = bcd_to_dec(data[4] & 0x3F)
    month = bcd_to_dec(data[5] & 0x1F)
    year = bcd_to_dec(data[6]) + 2000  # Корректировка года для DS3231
    
    print("Time: {}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        year, month, day, hour, minute, second))

# Чтение времени
read_time()
