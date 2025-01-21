# Video https://youtu.be/daVqzR42fFs
# Post http://kontakts.ru/showthread.php/40884?p=86160#post86160
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from dht import DHT11, InvalidChecksum
import time

# Инициализация I2C для дисплея и датчика
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Инициализация DHT11
DHT_pin = Pin(2, Pin.OUT, Pin.PULL_DOWN)
dht11 = DHT11(DHT_pin)

# Инициализация DS3231
rtc = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
ds3231_address = 0x68  # Адрес DS3231

# Функция для преобразования BCD в десятичное число
def bcd_to_dec(bcd):
    return (bcd & 0x0F) + ((bcd >> 4) * 10)

# Чтение времени с DS3231
def read_time():
    data = rtc.readfrom_mem(ds3231_address, 0x00, 7)  # Чтение 7 байтов данных
    second = bcd_to_dec(data[0] & 0x7F)
    minute = bcd_to_dec(data[1] & 0x7F)
    hour = bcd_to_dec(data[2] & 0x3F)
    day = bcd_to_dec(data[4] & 0x3F)
    month = bcd_to_dec(data[5] & 0x1F)
    year = bcd_to_dec(data[6]) + 2000  # Корректировка года для DS3231
    return year, month, day, hour, minute, second

# Основной цикл
if __name__ == '__main__':
    while True:
        try:
            # Чтение данных с датчика DHT11
            dht11.measure()  # Запуск измерений
            temp = dht11.temperature  # Получаем температуру в градусах Цельсия
            hum = dht11.humidity  # Получаем влажность в процентах

            # Чтение времени с DS3231
            year, month, day, hour, minute, second = read_time()

            # Форматирование времени и даты с ведущими нулями
            time_str = "Time: {:02}:{:02}:{:02}".format(hour, minute, second)  # Часы:минуты:секунды
            date_str = "Date: {:02}-{:02}-{:04}".format(day, month, year)  # День-месяц-год

            # Вывод данных на OLED дисплей
            oled.fill(0)  # Очищаем экран
            oled.text(time_str, 0, 0)  # Выводим время
            oled.text(date_str, 0, 10)  # Выводим дату
            oled.text("Temp: {} C".format(temp), 0, 20)  # Выводим температуру
            oled.text("Humi: {} %".format(hum), 0, 30)  # Выводим влажность
            oled.show()  # Обновляем экран

            # Вывод данных в монитор
            print(time_str)
            print(date_str)
            print("Temperature: {} C".format(temp))
            print("Humidity: {} %".format(hum))

        except InvalidChecksum:  # Обработка ошибки, если данные от датчика некорректны
            print("Checksum from the sensor was invalid")

        # Задержка 1 секунда
        time.sleep(1)
