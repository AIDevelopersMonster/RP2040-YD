 # Video https://youtu.be/iWITOycrXFE
# Post http://kontakts.ru/showthread.php/40884?p=86215#post86215
# Telega https://t.me/MrMicroPython 
from ws2812lib import ws2812b
from machine import Pin
import time

# Настроим пины для кнопок
left_button = Pin(14, Pin.IN, Pin.PULL_UP)  # Левая кнопка (по пину GP14)
right_button = Pin(15, Pin.IN, Pin.PULL_UP)  # Правая кнопка (по пину GP15)

# Массив из 16 основных цветов
colors = [
    (255, 0, 0),         # Красный
    (0, 255, 0),         # Зеленый
    (0, 0, 255),         # Синий
    (255, 255, 0),       # Желтый
    (0, 255, 255),       # Циан
    (255, 0, 255),       # Магента
    (255, 255, 255),     # Белый
    (0, 0, 0),           # Черный
    (255, 165, 0),       # Оранжевый
    (148, 0, 211),       # Фиолетовый
    (230, 230, 250),     # Лаванда
    (255, 192, 203),     # Розовый
    (245, 245, 220),     # Бежевый
    (144, 238, 144),     # Светло-зеленый
    (255, 218, 185),     # Персиковый
    (255, 255, 102),     # Лимонный
]

# Создаем объект для управления светодиодом на пине GP12
led = ws2812b(pin=12)

# Переменная для хранения индекса текущего цвета
current_color_index = 0

# Переменная для хранения яркости
current_brightness = 25  # Начальная яркость (50% от максимума)

# Функция для обновления цвета
def update_color():
    led.brightness(current_brightness)  # Устанавливаем яркость
    led.set_pixel(colors[current_color_index][0], colors[current_color_index][1], colors[current_color_index][2])
    led.show()

# Функция для обработки кнопок
def check_buttons():
    global current_color_index, current_brightness
    
    # Если нажата левая кнопка (перемещаемся назад)
    if left_button.value() == 0:  # кнопка нажата (активный низкий уровень)
        current_color_index -= 1
        if current_color_index < 0:
            current_color_index = len(colors) - 1  # Зацикливаем на последнем цвете
        update_color()
        time.sleep(0.3)  # Задержка для предотвращения дребезга

    # Если нажата правая кнопка (перемещаемся вперед)
    elif right_button.value() == 0:  # кнопка нажата
        current_color_index += 1
        if current_color_index >= len(colors):
            current_color_index = 0  # Зацикливаем на первом цвете
        update_color()
        time.sleep(0.3)  # Задержка для предотвращения дребезга

 

# Основной цикл
while True:
    check_buttons()
    time.sleep(0.1)  # Задержка для уменьшения загрузки процессора
