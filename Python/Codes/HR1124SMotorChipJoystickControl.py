# Video https://youtu.be/t_ZXlH4N5PQ
# Post http://kontakts.ru/showthread.php/40884?p=86174#post86174
# Telega https://t.me/MrMicroPython
from machine import Pin, ADC
import time

# Подключаем джойстик
joystick_x = ADC(Pin(26))  # Ось X (например, пин 26)
joystick_y = ADC(Pin(27))  # Ось Y (например, пин 27)

# Подключаем пины для мотора (например, пины 16 и 17)
motor1a = Pin(17, Pin.OUT)  # Направление 1
motor1b = Pin(16, Pin.OUT)  # Направление 2

# Функция для считывания значений с осей джойстика
def read_joystick():
    x_value = joystick_x.read_u16()  # Чтение оси X
    y_value = joystick_y.read_u16()  # Чтение оси Y
    return x_value, y_value

# Функция для управления мотором в зависимости от положения джойстика
def control_motor(x_value):
    # Управление направлением мотора в зависимости от значения оси X
    if 0 <= x_value <= 10000:
        # Включаем мотор в одну сторону (например, вперед)
        motor1a.high()
        motor1b.low()
        print("Motor Forward - Joystick X:", x_value)
    elif 50000 <= x_value <= 65535:
        # Включаем мотор в другую сторону (например, назад)
        motor1a.low()
        motor1b.high()
        print("Motor Backward - Joystick X:", x_value)
    else:
        # Останавливаем мотор, если значение вне указанных диапазонов
        motor1a.low()
        motor1b.low()
        print("Motor Stopped - Joystick X:", x_value)

def test():
    while True:
        # Считываем значения джойстика
        x_value, y_value = read_joystick()
        
        # Контролируем мотор в зависимости от значения оси X
        control_motor(x_value)
        
        # Выводим значения в консоль
        print("Joystick X Position:", x_value)
        print("Joystick Y Position:", y_value)

        # Задержка для обновления значений
        time.sleep(0.1)

# Запуск теста
test()
