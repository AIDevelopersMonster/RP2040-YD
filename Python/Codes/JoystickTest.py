# Video https://youtu.be/pltAmwSWYRw
# Post http://kontakts.ru/showthread.php/40884?p=86173#post86173
from machine import Pin, ADC
import time

# Создаем объекты для подключения к осям X и Y джойстика
joystick_x = ADC(Pin(26))  # Ось X (например, пин 26)
joystick_y = ADC(Pin(27))  # Ось Y (например, пин 27)

# Создаем объект для кнопки джойстика с подтяжкой вверх
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Кнопка подключена к пину 14 (с подтяжкой вверх)

def read_joystick():
    x_value = joystick_x.read_u16()  # Считываем значение по оси X
    y_value = joystick_y.read_u16()  # Считываем значение по оси Y
    return x_value, y_value

def read_button():
    return button.value() == 1  # Кнопка нажата, если на пине низкий уровень (0)

def test():
    while True:
        # Считываем значения с джойстика
        x_value, y_value = read_joystick()
        
        # Проверяем, нажата ли кнопка
        button_state = read_button()

        # Выводим значения в консоль
        print("Joystick X Position:", x_value)
        print("Joystick Y Position:", y_value)
        
        # Проверяем состояние кнопки
        if button_state:
            print("Button Pressed!")
        else:
            print("Button Not Pressed")

        # Задержка для обновления значений
        time.sleep(0.1)

# Запуск теста
test()
