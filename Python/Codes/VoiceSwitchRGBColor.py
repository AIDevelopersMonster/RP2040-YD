# Video https://youtu.be/yaa6MG0j_YE
# Post  http://kontakts.ru/showthread.php/40884?p=86125#post86125

from machine import Pin, PWM
import utime

# Инициализация RGB светодиодов с использованием PWM
Led_R = PWM(Pin(2))  # Красный светодиод на пине 2
Led_G = PWM(Pin(3))  # Зелёный светодиод на пине 3
Led_B = PWM(Pin(4))  # Синий светодиод на пине 4

# Инициализация микрофонного датчика с цифровым выходом (с компаратором)
mic_input = Pin(0, Pin.IN)  # Пин для цифрового сигнала от микрофона (GPIO1)

# Устанавливаем частоту PWM для всех светодиодов
Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)

# Состояние переключателя для цветов
color_state = 0  # Начальное состояние (выключено)

# Функция для включения/выключения светодиодов
def set_color(state):
    if state == 0:
        Led_R.duty_u16(0)  # Выключаем красный
        Led_G.duty_u16(0)  # Выключаем зелёный
        Led_B.duty_u16(0)  # Выключаем синий
    elif state == 1:
        Led_R.duty_u16(65535)  # Включаем красный
        Led_G.duty_u16(0)  # Выключаем зелёный
        Led_B.duty_u16(0)  # Выключаем синий
    elif state == 2:
        Led_R.duty_u16(0)  # Выключаем красный
        Led_G.duty_u16(65535)  # Включаем зелёный
        Led_B.duty_u16(0)  # Выключаем синий
    elif state == 3:
        Led_R.duty_u16(0)  # Выключаем красный
        Led_G.duty_u16(0)  # Выключаем зелёный
        Led_B.duty_u16(65535)  # Включаем синий

# Главная программа
if __name__ == "__main__":
    while True:
        if mic_input.value() == 1:  # Когда с компаратора на выходе высокий уровень (звук)
            utime.sleep_ms(200)  # Задержка для предотвращения дребезга
            color_state = (color_state + 1) % 4  # Переключаем состояние от 0 до 3

        set_color(color_state)  # Устанавливаем текущий цвет

        utime.sleep_ms(100)
