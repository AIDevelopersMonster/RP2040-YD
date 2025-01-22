# Video https://youtu.be/QMJUrI8iiE0
# Post http://kontakts.ru/showthread.php/40884?p=86170#post86170
from machine import Pin
import time

# Настроим пин для зуммера на 16-й пин
buzzer = Pin(16, Pin.OUT)

# Пример звуковых паттернов для зуммера
sounds = {
    "button_press": [200, 200],  # 2 коротких пика
    "button_held": [1000],       # 1 длинный пик
    "error_alarm": [200, 200, 200, 1000],  # 3 коротких пика
    "warning": [200, 1000],      # Прерывистый сигнал
    "alarm": [500, 500, 500, 1000], # Тревожный сигнал
    "system_start": [300, 300],  # 2 коротких пика
    "task_completed": [1000],    # 1 длинный пик
    "low_battery": [300, 300, 300, 1000], # Мелодия низкого заряда
    "system_crash": [1000, 1000, 1000], # Системный сбой
    "device_on": [500, 1000],   # Включение устройства
    "system_check": [300, 300, 300, 300], # Проверка системы
    "memory_error": [500, 300, 500, 1000], # Ошибки памяти
    "connection_established": [300, 1000], # Подключение завершено
    "update_in_progress": [200, 500, 200], # Обновление
    "idle_mode": [200, 200, 200, 500],  # Режим ожидания
}

# Функция для воспроизведения звукового паттерна
def play_sound(pattern):
    print(f"Playing pattern: {pattern}")  # Выводим название паттерна на монитор
    for duration in sounds[pattern]:
        buzzer.on()
        time.sleep(duration / 1000)  # Пик длится "duration" миллисекунд
        buzzer.off()
        time.sleep(0.1)  # Небольшая пауза между пиками

# Основной цикл для перебора всех паттернов
while True:
    for pattern in sounds:
        play_sound(pattern)  # Воспроизведение текущего паттерна
        time.sleep(1)  # Задержка между воспроизведениями
