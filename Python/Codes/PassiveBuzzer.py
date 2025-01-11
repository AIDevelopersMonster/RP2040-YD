from machine import Pin, PWM
from time import sleep

# Пин для подключения пассивного базера
buzzer = Pin(15, Pin.OUT)
buzzer_pwm = PWM(buzzer)

# Частоты нот (в Гц)
NOTES = {
    'C4': 261, 'C5': 523, 'D4': 293, 'D5': 587, 
    'E4': 329, 'E5': 659, 'F4': 349, 'F5': 698, 
    'G4': 392, 'G5': 784, 'A4': 440, 'A5': 880, 
    'B4': 466, 'AS4': 466, 'AS5': 932
}

# Мелодия и длительности
melody = [
    'C4', 'A4', 'A4', 'G4', 'A4', 'F4', 'C4', 'C4',
    'C4', 'A4', 'A4', 'AS4', 'G4', 'C5', 'C5', 'D4',
    'D4', 'AS4', 'AS4', 'A4', 'G4', 'F4', 'C4', 'A4',
    'A4', 'G4', 'A4', 'F4'
]

durations = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
             4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 
             4, 4, 4, 4, 4, 2]

# Установка частоты для генерации звуков
def play_tone(note, duration):
    if note in NOTES:
        buzzer_pwm.freq(NOTES[note])  # Устанавливаем частоту для этой ноты
        buzzer_pwm.duty_u16(32768)  # Устанавливаем среднюю громкость
        sleep(duration)  # Длительность ноты
        buzzer_pwm.duty_u16(0)  # Останавливаем звук

# Основной цикл
def play_melody():
    for _ in range(2):  # Повторяем дважды
        for i in range(len(melody)):
            note = melody[i]
            duration = 1 / durations[i]  # Длительность в секундах
            play_tone(note, duration)  # Играем ноту
            sleep(0.1)  # Пауза между нотами
        sleep(0.2)  # Пауза после окончания одной мелодии
    sleep(6)  # Пауза после двух повторов мелодии

# Запуск мелодии
play_melody()
