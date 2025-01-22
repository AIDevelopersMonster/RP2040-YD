# Video https://youtu.be/qIABUL9IpOs
# Post http://kontakts.ru/showthread.php/40884?p=86171#post86171
from machine import Pin
import time
import random  # Модуль для генерации случайных чисел

# Инициализация пинов для датчика PIR, светодиода и зуммера
sensor_pir = Pin(2, Pin.IN)   # Датчик PIR на пине 2
led = Pin(22, Pin.OUT)         # Светодиод на пине 22
buzzer = Pin(19, Pin.OUT)      # Зуммер на пине 19

# База звуков для активного зуммера
sounds = {
    'button_press': [0.1, 0.1, 0.1],   # Короткий сигнал для нажатия кнопки
    'alarm': [0.5, 0.5, 0.5, 0.5],    # Прерывистый тревожный сигнал
    'task_completed': [0.3, 0.3, 0.3],  # Долгий сигнал по завершению задачи
    'low_battery': [0.2, 0.2, 0.1],    # Звук для уведомления о низком заряде
    'system_error': [0.1, 0.1, 0.5],   # Звук ошибки системы
}

# Функция для воспроизведения случайного звука
def play_random_sound():
    # Выбираем случайный звук из базы
    sound_key = random.choice(list(sounds.keys()))
    sound_pattern = sounds[sound_key]
    print(f"Playing sound: {sound_key}")  # Печатаем название звука для диагностики

    # Воспроизведение выбранного звука
    for duration in sound_pattern:
        buzzer.on()
        time.sleep(duration)
        buzzer.off()
        time.sleep(duration)

# Обработчик прерывания для PIR датчика
def pir_handler(pin): 
    print("ALARM! Motion detected!")  # Сообщение при обнаружении движения
    play_random_sound()  # Воспроизведение случайного звука при срабатывании датчика
    for i in range(50): 
        led.toggle()   # Переключение состояния светодиода
        buzzer.toggle() # Переключение состояния зуммера
        time.sleep_ms(100)  # Пауза в 100 миллисекунд для создания мигающего эффекта

# Настройка прерывания на датчик PIR
sensor_pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

# Главный цикл программы
while True:
    led.toggle()   # Переключаем состояние светодиода
    time.sleep(5)  # Пауза 5 секунд перед следующим циклом
