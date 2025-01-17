# Video https://youtu.be/JnlCvDAuN9M
# Post http://kontakts.ru/showthread.php/40884?p=86152#post86152
# Напишите здесь свой код :-)
from machine import Pin, I2C
import time
import tm1637

# Инициализация I2C с назначением пинов
i2c = I2C(0, sda=Pin(0), scl=Pin(1))

# Адрес DS3231
address = 0x68

# Инициализация 7-сегментного дисплея HW-069 (CLK - Pin(2), DIO - Pin(3))
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(3))

# Функция преобразования BCD в десятичное число
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
    
    # Отображение времени на 7-сегментном дисплее
    # Отображаем только часы и минуты (формат HHMM)
    tm.numbers(hour, minute)

# Чтение времени и отображение на дисплее
while True:
    read_time()
    time.sleep(1)
