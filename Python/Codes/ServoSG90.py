# Video https://youtu.be/HhoNVFfJqwY
# Post http://kontakts.ru/showthread.php/40884?p=86142#post86142
from machine import Pin, PWM
from time import sleep

# Создаем объект PWM на пине 0 с частотой 50 Гц
servo = PWM(Pin(0), freq=50)

while True:
    # Перемещение серво от 0 до 180 градусов (имитация)
    for duty_cycle in range(0, 8000, 10):  # Примерный диапазон для 0-180 градусов
        servo.duty_u16(duty_cycle)  # Устанавливаем ширину импульса
        sleep(0.002)  # Пауза 20 мс (частота 50 Гц)

    # Перемещение серво от 180 до 0 градусов
    for duty_cycle in range(8000, 0, -10):
        servo.duty_u16(duty_cycle)  # Устанавливаем ширину импульса
        sleep(0.002)  # Пауза 20 мс (частота 50 Гц)
