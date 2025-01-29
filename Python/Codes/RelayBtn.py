# Video https://youtu.be/9gQi42ewuco
# Post http://kontakts.ru/showthread.php/40884?p=86196#post86196
# Telega https://t.me/MrMicroPython
# Напишите здесь свой код :-)
from machine import Pin
import time

# Инициализация реле на пине 16, установка его как выход
relay = Pin(16, Pin.OUT)

# Инициализация кнопки на пине 15, установка его как вход с подтяжкой к питанию (pull-up)
button = Pin(15, Pin.IN, Pin.PULL_UP)

# Флаг состояния реле
relay_state = False

# Функция включения реле (COM и NO соединяются, COM и NC размыкаются)
def relay_on():
    relay.value(1)

# Функция выключения реле (COM и NO размыкаются, COM и NC соединяются)
def relay_off():
    relay.value(0)

# Основной цикл программы
while True:
    # Проверяем, нажата ли кнопка (LOW-сигнал, так как pull-up)
    if button.value() == 0:
        time.sleep(0.05)  # Дебаунс (защита от дребезга контактов)
        
        # Повторная проверка после задержки, чтобы убедиться, что кнопка действительно нажата
        if button.value() == 0:
            # Изменяем состояние реле (переключение)
            relay_state = not relay_state
            relay.value(relay_state)
            
            # Ожидаем отпускания кнопки, чтобы избежать многократного срабатывания
            while button.value() == 0:
                time.sleep(0.05)

    time.sleep(0.05)  # Маленькая задержка для стабильной работы
