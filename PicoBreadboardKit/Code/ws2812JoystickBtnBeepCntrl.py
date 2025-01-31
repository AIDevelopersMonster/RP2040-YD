 # Video https://youtu.be/S5txzF9cs-s
# Post http://kontakts.ru/showthread.php/40884?p=86218#post86218
# Telega https://t.me/MrMicroPython 
from ws2812lib import ws2812b
from machine import Pin, PWM, ADC
import time

# Настроим пины для кнопок и Beeper
left_button = Pin(14, Pin.IN, Pin.PULL_UP)  # Левая кнопка (по пину GP14)
right_button = Pin(15, Pin.IN, Pin.PULL_UP)  # Правая кнопка (по пину GP15)
beeper = Pin(13, Pin.OUT)  # Пин для Beeper (GP13)
beeper_pwm = PWM(beeper)  # Настроим PWM для Beeper

# Настроим пины для джойстика (X и Y оси)
joystick_x = ADC(0)  # X ось джойстика (ADC0)
joystick_y = ADC(1)  # Y ось джойстика (ADC1)

# Настроим пины для светодиодов D1 и D2
left_led = Pin(16, Pin.OUT)  # Светодиод для левой кнопки на GP16
right_led = Pin(17, Pin.OUT)  # Светодиод для правой кнопки на GP17

# Создаем объект для управления светодиодом на пине GP12
led = ws2812b(pin=12)

# Переменная для хранения текущего цвета
current_color = (0, 0, 0)  # Начальный цвет (черный)
brightness = 128  # Начальная яркость (половина максимальной яркости)

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

# Функция для обновления цвета светодиода в зависимости от джойстика
def update_color_from_joystick():
    x_value = joystick_x.read_u16()  # Чтение значения с X оси
    y_value = joystick_y.read_u16()  # Чтение значения с Y оси

    # Преобразуем показания джойстика в цвет (с масштабированием в диапазон 0-255)
    red = int((x_value / 65535) * 255)  # Маппинг X оси на красный цвет
    green = int((y_value / 65535) * 255)  # Маппинг Y оси на зеленый цвет
    blue = 255 - (red + green) // 2  # Синий цвет зависит от красного и зеленого

    return (red, green, blue)

# Функция для обновления цвета на светодиоде с учетом яркости
def update_led_color():
    global current_color, brightness
    red, green, blue = update_color_from_joystick()  # Получаем цвет от джойстика

    # Применяем яркость к каждому цвету
    red = int((red * brightness) / 255)
    green = int((green * brightness) / 255)
    blue = int((blue * brightness) / 255)

    current_color = (red, green, blue)
    led.set_pixel(red, green, blue)  # Применяем цвет
    led.show()

# Функция для обработки кнопок
def check_buttons():
    global brightness

    # Если нажата левая кнопка (уменьшаем яркость)
    if right_button.value() == 0:  # кнопка нажата (активный низкий уровень)
        brightness = max(0, brightness - 5)  # Уменьшаем яркость, но не меньше 0
        short_beep()  # Воспроизводим короткий звук при изменении яркости
        right_led.value(1)  # Включаем светодиод для левой кнопки
    else:
        right_led.value(0)  # Выключаем светодиод для левой кнопки

    # Если нажата правая кнопка (увеличиваем яркость)
    if left_button.value() == 0:  # кнопка нажата
        brightness = min(255, brightness + 5)  # Увеличиваем яркость, но не больше 255
        short_beep()  # Воспроизводим короткий звук при изменении яркости
        left_led.value(1)  # Включаем светодиод для правой кнопки
    else:
        left_led.value(0)  # Выключаем светодиод для правой кнопки

# Воспроизведение мелодии при запуске
play_startup_melody()

# Основной цикл
while True:
    update_led_color()  # Обновляем цвет в зависимости от джойстика и яркости
    time.sleep(0.1)  # Задержка для уменьшения загрузки процессора
    check_buttons()  # Проверяем состояние кнопок
