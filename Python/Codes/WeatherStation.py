# Video https://youtu.be/8d8kcPs00Zk
# Post http://kontakts.ru/showthread.php/40884?p=86157#post86157
from machine import I2C, Pin                # Импортируем необходимые модули для работы с I2C и пинами
from i2c_lcd import I2cLcd                 # Импортируем библиотеку для работы с LCD
from utime import sleep                    # Импортируем sleep для задержек
from dht import DHT11, InvalidChecksum     # Импортируем DHT11 сенсор и исключение для некорректных данных

DEFAULT_I2C_ADDR = 0x27                   # Адрес I2C для LCD 1602
led_red = Pin(4, Pin.OUT)                  # Красный светодиод для индикации высокой температуры или низкой влажности
led_green = Pin(5, Pin.OUT)                # Зеленый светодиод для нормальных значений температуры и влажности
pin = Pin(2, Pin.OUT, Pin.PULL_DOWN)       # Пин для подключения DHT11
dht11 = DHT11(pin)                        # Инициализация сенсора DHT11

def setup():
    global lcd 
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)  # Настройка I2C интерфейса (SDA на пине 0, SCL на пине 1)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)           # Инициализация LCD с 2 строками и 16 символами на строку

def loop():
    try:
        while True:
            # Чтение данных с DHT11
            dht11.measure()                                # Получаем показания с датчика
            temp = dht11.temperature                        # Температура в градусах Цельсия
            hum = dht11.humidity                           # Влажность в процентах

            # Выводим температуру с символом термометра и градусами Цельсия
            lcd.move_to(0, 0)                              # Перемещаем курсор в начало первой строки
            lcd.putstr("Temp: {} C ".format(temp))         # Форматируем вывод температуры с символом °C (градусы Цельсия)

            # Выводим влажность с символом капельки и процентами
            lcd.move_to(0, 1)                              # Перемещаем курсор во вторую строку
            lcd.putstr("Humi: {} % ".format(hum))           # Форматируем вывод влажности с символом %

            # Условие для индикации на основе показаний температуры и влажности
            if temp > 25 or hum < 10:                      # Если температура больше 35 или влажность меньше 10%
                led_red.value(1)                           # Включаем красный светодиод
                led_green.value(0)                         # Выключаем зеленый светодиод
                sleep(0.5)
                led_red.value(0)                           # Выключаем красный светодиод
                sleep(0.5)
            else:
                led_red.value(0)                           # Выключаем красный светодиод
                led_green.value(1)                         # Включаем зеленый светодиод

            sleep(1)                                       # Задержка 1 секунда
            lcd.clear()                                    # Очищаем экран перед следующей итерацией

    except InvalidChecksum:  # Обработка ошибки, если данные от датчика некорректны
        print("Checksum from the sensor was invalid")

# Основная часть программы
if __name__ == '__main__':
    setup()  # Настройка LCD и сенсора
    loop()   # Запуск основного цикла
