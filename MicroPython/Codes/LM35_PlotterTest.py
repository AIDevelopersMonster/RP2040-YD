# Video https://youtu.be/uadDWUCNeHg
# Post http://kontakts.ru/showthread.php/40884?p=86199#post86199
# Telega https://t.me/MrMicroPython
from machine import ADC, Pin
import time

# Настройка пина для LM35 (GPIO 26 - ADC0)
lm35 = ADC(26)

# Функция для получения температуры с LM35
def read_temp():
    # Чтение аналогового значения с LM35
    voltage = lm35.read_u16() * (3.3 / 65535)  # Перевод в вольты
    temp = voltage * 100  # LM35: 10 мВ = 1°C
    return temp  # Возвращаем температуру как float (с плавающей запятой)

# Основной цикл
while True:
    temp = read_temp()  # Получаем температуру
    # Выводим температуру как кортеж с одним элементом (флот)
    print((temp,))  # Кортеж с одним элементом, который является температурой
    time.sleep(1)  # Задержка в 1 секунду
