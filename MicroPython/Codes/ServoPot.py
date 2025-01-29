# Video https://youtu.be/_aplwOxeBaE
# Post http://kontakts.ru/showthread.php/40884?p=86143#post86143
from time import sleep
from machine import Pin, PWM, ADC

# Инициализация PWM на пине 0 с частотой 50 Гц
pwm = PWM(Pin(0))
pwm.freq(50)

# Инициализация потенциометра на пине GP26 (ADC0)
potentiometer = ADC(Pin(26))

# Функция для установки угла серво
def setServoCycle(position):
    pwm.duty_u16(position)  # Устанавливаем ширину импульса
    sleep(0.02)  # Пауза для стабилизации

while True:
    # Считываем значение с потенциометра (диапазон 0-65535)
    pot_value = potentiometer.read_u16()

    # Выводим значение потенциометра в консоль
    print("Потенциометр:", pot_value)

    # Преобразуем значение потенциометра в диапазон от 0 до 8000 для серво
    # Для серво SG90 обычно применяется диапазон от 500 до 2700
    # Здесь для упрощения будет использоваться диапазон от 0 до 8000
    servo_position = int(pot_value * 8000 / 65535)

    # Устанавливаем новое положение серво
    setServoCycle(servo_position)

    sleep(0.1)  # Пауза для обновления значения
