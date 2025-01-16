# Video https://youtu.be/ivr4pP-nU7w
# Post ?p=86145#post86145
from time import sleep
from machine import Pin, PWM, ADC

# Инициализация PWM на пине 0 с частотой 50 Гц
pwm = PWM(Pin(0))
pwm.freq(50)

# Инициализация джойстика на пинах GP26 (ADC0) и GP27 (ADC1)
joystick_x = ADC(Pin(26))  # для оси X
joystick_y = ADC(Pin(27))  # для оси Y

# Функция для установки угла серво
def setServoCycle(position):
    pwm.duty_u16(position)  # Устанавливаем ширину импульса
    sleep(0.02)  # Пауза для стабилизации

# Функция для маппинга значений
def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    # Считываем значения с оси X (для угла)
    joystick_x_value = joystick_x.read_u16()

    # Преобразуем значение джойстика в диапазоны для сервопривода
    if joystick_x_value < 32768:
        # Если джойстик повернут в одну сторону, маппируем от 8000 до 4000
        servo_position = map_range(joystick_x_value, 0, 32767, 8000, 4000)
    else:
        # Если в другую сторону, маппируем от 4000 до 900
        servo_position = map_range(joystick_x_value, 32767, 65535, 4000, 900)

    # Устанавливаем новое положение серво
    setServoCycle(servo_position)

    # Выводим значение для отладки
    print(f"Joystick X: {joystick_x_value}, Servo Position: {servo_position}")

    sleep(0.1)  # Пауза перед обновлением значений
   
