from machine import Pin, PWM
from time import sleep

# Пин для подключения пассивного базера
buzzer = Pin(15, Pin.OUT)
buzzer_pwm = PWM(buzzer)

# Функция для воспроизведения тревожной сирены (Alarm)
def alarm_sound():
    while True:
        # Быстрое изменение частоты для имитации тревожного сигнала
        for i in range(5):  # Пять циклов звука тревоги
            buzzer_pwm.freq(1000)  # Высокая частота
            buzzer_pwm.duty_u16(32768)  # Средняя громкость
            sleep(0.1)  # Пауза для высокой частоты

            buzzer_pwm.freq(500)  # Низкая частота
            buzzer_pwm.duty_u16(32768)  # Средняя громкость
            sleep(0.1)  # Пауза для низкой частоты

        sleep(1)  # Пауза перед повтором

# Запуск тревожного сигнала
alarm_sound()
