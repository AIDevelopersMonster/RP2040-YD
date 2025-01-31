 # Video https://youtu.be/1vDn_Vh4Dsw
# Post http://kontakts.ru/showthread.php/40884?p=86216#post86216
# Telega https://t.me/MrMicroPython 
from ws2812lib import ws2812b
from machine import Pin, PWM
import time

# Настроим пины для кнопок и Beeper
left_button = Pin(14, Pin.IN, Pin.PULL_UP)  # Левая кнопка (по пину GP14)
right_button = Pin(15, Pin.IN, Pin.PULL_UP)  # Правая кнопка (по пину GP15)
beeper = Pin(13, Pin.OUT)  # Пин для Beeper (GP13)
beeper_pwm = PWM(beeper)  # Настроим PWM для Beeper

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

# Функция для обновления цвета с учетом яркости
def update_color():
    brightness = 20  # Устанавливаем яркость 20 (измените это значение по желанию)
    led.brightness(brightness)  # Применяем яркость
    led.set_pixel(colors[current_color_index][0], colors[current_color_index][1], colors[current_color_index][2])
    led.show()

# Функция для воспроизведения короткого звука
def short_beep():
    beeper_pwm.duty_u16(32767)  # Устанавливаем среднюю громкость
    time.sleep(0.1)  # Короткий звук
    beeper_pwm.duty_u16(0)  # Выключаем звук

# Функция для воспроизведения мелодии при запуске
def play_startup_melody():
    melody = [523, 659, 784, 880, 1047]  # Частоты нот (C4, E4, G4, A4, C5)
    for note in melody:
        beeper_pwm.freq(note)  # Устанавливаем частоту
        beeper_pwm.duty_u16(32767)  # Включаем звук
        time.sleep(0.3)  # Длительность ноты
        beeper_pwm.duty_u16(0)  # Выключаем звук
        time.sleep(0.1)  # Пауза между нотами

# Функция для обработки кнопок
def check_buttons():
    global current_color_index
    
    # Если нажата левая кнопка (перемещаемся назад)
    if left_button.value() == 0:  # кнопка нажата (активный низкий уровень)
        current_color_index -= 1
        if current_color_index < 0:
            current_color_index = len(colors) - 1  # Зацикливаем на последнем цвете
        update_color()
        short_beep()  # Воспроизводим короткий звук при изменении цвета
        time.sleep(0.3)  # Задержка для предотвращения дребезга

    # Если нажата правая кнопка (перемещаемся вперед)
    elif right_button.value() == 0:  # кнопка нажата
        current_color_index += 1
        if current_color_index >= len(colors):
            current_color_index = 0  # Зацикливаем на первом цвете
        update_color()
        short_beep()  # Воспроизводим короткий звук при изменении цвета
        time.sleep(0.3)  # Задержка для предотвращения дребезга

# Воспроизведение мелодии при запуске
play_startup_melody()

# Основной цикл
while True:
    check_buttons()
    time.sleep(0.1)  # Задержка для уменьшения загрузки процессора
# Напишите здесь свой код :-)
