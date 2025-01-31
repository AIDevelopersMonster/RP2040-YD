from ws2812lib import ws2812b
import time

# Настроим библиотеку для работы с одним светодиодом
led = ws2812b(pin=12)  # Используем пин GP12, куда подключен WS2812

# Пример: смена цветов с задержкой 1 секунда
while True:
    led.set_pixel(255, 0, 0)  # Красный
    led.show()
    time.sleep(1)

    led.set_pixel(0, 255, 0)  # Зеленый
    led.show()
    time.sleep(1)

    led.set_pixel(0, 0, 255)  # Синий
    led.show()
    time.sleep(1)
