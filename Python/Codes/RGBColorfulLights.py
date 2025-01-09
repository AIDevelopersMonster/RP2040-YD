from machine import Pin, PWM
import utime
import random

# Инициализация RGB светодиодов с использованием PWM
Led_R = PWM(Pin(2))  # Красный светодиод на пине 2
Led_G = PWM(Pin(3))  # Зелёный светодиод на пине 3
Led_B = PWM(Pin(4))  # Синий светодиод на пине 4

# Устанавливаем частоту PWM для всех светодиодов
# Video
# Post
Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)

# Функция для плавного изменения яркости
def fade_led(led, start, end, steps=50):
    step_size = (end - start) / steps  # Шаг изменения яркости
    for i in range(steps):
        current_value = int(start + i * step_size)  # Текущее значение яркости
        led.duty_u16(current_value)  # Устанавливаем яркость
        utime.sleep_ms(10)  # Задержка для плавности изменения

# Главная программа
if __name__ == "__main__":
    while True:
        # Генерация случайных значений яркости для каждого канала (от 0 до 65535)
        R = random.randint(0, 65535)
        G = random.randint(0, 65535)
        B = random.randint(0, 65535)

        # Плавное изменение яркости каждого канала
        fade_led(Led_R, Led_R.duty_u16(), R)  # Плавно меняем красный
        fade_led(Led_G, Led_G.duty_u16(), G)  # Плавно меняем зелёный
        fade_led(Led_B, Led_B.duty_u16(), B)  # Плавно меняем синий

        # Задержка перед следующей сменой цвета
        utime.sleep_ms(100)
