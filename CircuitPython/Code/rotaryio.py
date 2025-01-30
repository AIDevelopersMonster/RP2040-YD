# Video https://youtu.be/XvvTKivE40c
# Post http://kontakts.ru/showthread.php/40884?p=86203#post86203
# Telega https://t.me/MrMicroPython
# 📜 Лицензия 🔗 Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
# 📂 Оригинальный код для платы PicoMate https://wiki.deskpi.com/picomate/#pinout-diagram
import rotaryio  # Модуль для работы с энкодером
import board  # Модуль для доступа к пинам микроконтроллера
import digitalio  # Модуль для работы с цифровыми входами/выходами

# Инициализация энкодера на пинах GP7 и GP6
encoder = rotaryio.IncrementalEncoder(board.GP7, board.GP6)

# Инициализация кнопки, связанной с энкодером, на пине GP26
switch = digitalio.DigitalInOut(board.GP26)
switch.direction = digitalio.Direction.INPUT  # Устанавливаем пин как вход
switch.pull = digitalio.Pull.DOWN  # Включаем подтягивающий резистор к GND (Pull.DOWN)

# Переменные для хранения предыдущих значений
last_position = encoder.position  # Начальное положение энкодера
switch_state = switch.value  # Начальное состояние кнопки

# Основной цикл для отслеживания вращения энкодера и состояния кнопки
while True:
    # Чтение текущего положения энкодера
    position = encoder.position

    # Проверка изменения положения энкодера
    if last_position is None or position != last_position:
        print(f"Rotary: {position}")  # Выводим текущее положение энкодера

    # Обновление предыдущего положения
    last_position = position

    # Проверка изменения состояния кнопки
    if switch_state != switch.value:
        switch_state = switch.value  # Обновление предыдущего состояния кнопки
        # Выводим текущее состояние кнопки: ON (нажата) или OFF (отпущена)
        print('Switch is ' + ('ON' if switch.value else 'OFF'))
