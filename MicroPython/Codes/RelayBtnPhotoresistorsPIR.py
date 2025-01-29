# Video https://youtu.be/Q8YzDCzPAGQ
# Post http://kontakts.ru/showthread.php/40884?p=86198#post86198
# Telega https://t.me/MrMicroPython
from machine import Pin, ADC
import time

# Инициализация реле
relay = Pin(16, Pin.OUT)

# Кнопка (включает/выключает автоматический режим)
button = Pin(15, Pin.IN, Pin.PULL_UP)

# Фоторезистор (ADC0 - GPIO26)
photoresistor = ADC(26)

# PIR-датчик движения (GPIO14)
pir_sensor = Pin(14, Pin.IN)

# Флаг автоматического режима
auto_mode = False

# Пороговые значения освещенности
THRESHOLD_ON = 2000  # Включение при темноте
THRESHOLD_OFF = 8000  # Выключение при ярком свете

# Переменная состояния реле
relay_state = False

# Функции управления реле
def relay_on():
    global relay_state
    relay.value(1)
    relay_state = True

def relay_off():
    global relay_state
    relay.value(0)
    relay_state = False

# Основной цикл работы
while True:
    # Читаем освещенность
    light_level = photoresistor.read_u16()

    # Проверяем движение (1 - движение, 0 - нет)
    motion_detected = pir_sensor.value()

    # Вывод информации в монитор
    print(f"🌞 Освещенность: {light_level} | 🚶 Движение: {'Да' if motion_detected else 'Нет'} | 🎛️ Режим: {'Авто' if auto_mode else 'Выкл'} | 💡 Реле: {'🔥' if relay_state else '❌'}")

    # Проверяем кнопку (переключает авто-режим)
    if button.value() == 0:
        time.sleep(0.05)  # Дебаунс
        if button.value() == 0:  # Повторная проверка
            auto_mode = not auto_mode
            print(f"🎛️ Авто-режим {'Включен' if auto_mode else 'Выключен'}")
            while button.value() == 0:
                time.sleep(0.05)

    # Логика работы в автоматическом режиме
    if auto_mode:
        if light_level < THRESHOLD_ON and motion_detected and not relay_state:
            relay_on()
            print("🌑 Темно + Движение! 💡 Реле ВКЛЮЧЕНО!")

        elif light_level > THRESHOLD_OFF and relay_state:
            relay_off()
            print("☀️ Светло! 💡 Реле ВЫКЛЮЧЕНО!")
    else:
        relay_off()

    time.sleep(0.5)  # Задержка для стабильности
