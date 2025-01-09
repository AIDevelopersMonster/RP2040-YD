# Video https://youtu.be/g2b9v4ZtzKs
# Post http://kontakts.ru/showthread.php/40884?p=86122#post86122
from machine import Pin  # Импортируем класс для работы с пинами
import utime  # Импортируем модуль для работы с задержками

# Создаем список объектов Pin для пинов 0, 1, 2, 3, 4
# Каждый пин настроен как выходной (Pin.OUT)
leds = [Pin(i, Pin.OUT) for i in range(0, 29)]

if __name__ == '__main__':
    while True:  # Главный бесконечный цикл
        # Включаем светодиоды поочередно с интервалом в 50 миллисекунд
        for n in range(0, 29):
            leds[n].value(1)  # Включаем текущий светодиод
            utime.sleep_ms(50)  # Задержка 50 миллисекунд

        # Выключаем светодиоды поочередно с интервалом в 50 миллисекунд
        for n in range(0, 29):
            leds[n].value(0)  # Выключаем текущий светодиод
            utime.sleep_ms(50)  # Задержка 50 миллисекунд
