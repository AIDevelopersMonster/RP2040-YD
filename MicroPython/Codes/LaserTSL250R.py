# Video https://youtu.be/tM3XkLIygSY
# Post http://kontakts.ru/showthread.php/40884?p=86130#post86130
from machine import Pin, ADC
import time

# Настройка пина для лазерного модуля (выход)
laser = Pin(15, Pin.OUT)

# Настройка АЦП для датчика TSL250R (например, на GPIO26)
photo_sensor = ADC(Pin(26))

# Включение лазера
laser.value(1)  # Лазер включен

# Основной цикл
while True:
    # Чтение аналогового значения с датчика
    sensor_value = photo_sensor.read_u16()  # Значение от 0 до 65535

    # Преобразование в более удобный диапазон
    sensor_voltage = sensor_value * 3.3 / 65535  # Переводим в вольты (Pi Pico работает от 3.3 В)

    print("Чтение с датчика:", sensor_value, "Напряжение:", sensor_voltage)

    # Простая логика на основе значений
    if sensor_voltage > 1.0:  # Пороговое значение для обнаружения лазера
        print("Лазерный луч обнаружен!")
    else:
        print("Лазерный луч не обнаружен.")
    
    time.sleep(0.5)  # Пауза 0.5 секунды
