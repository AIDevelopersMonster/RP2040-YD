# Video https://www.youtube.com/watch?v=5Mzvnbpra8k
# Post http://kontakts.ru/showthread.php/40884?p=86138#post86138
from machine import Pin, ADC, PWM, UART
from time import sleep
import math

# Пины для подключения датчика влажности почвы и светодиодов
Soil_moisture_pin = 26        # ADC0 multiplexing pin is GP26 (Пин для датчика влажности почвы)
buzzer = PWM(Pin(12))         # Пин для подключения зуммера (buzzer)
Led_R = PWM(Pin(2))           # Красный светодиод
Led_G = PWM(Pin(3))           # Зеленый светодиод
Led_B = PWM(Pin(4))           # Синий светодиод

# Устанавливаем частоту для всех PWM пинов (светодиодов)
Led_R.freq(2000)  
Led_G.freq(2000)   
Led_B.freq(2000)   

# Настройка последовательного порта для вывода значений
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))  # Используем UART1 с TX на пине 4 и RX на пине 5

# Функция для настройки объекта ADC (аналогового входа) для датчика влажности
def setup():
    global Moisture
    Moisture = ADC(Soil_moisture_pin)  # Инициализация ADC для считывания значений с датчика влажности

# Функция для воспроизведения звука на зуммере
def playtone(frequency):
    buzzer.duty_u16(1000)  # Устанавливаем громкость
    buzzer.freq(frequency) # Устанавливаем частоту сигнала зуммера
    
# Функция для выключения звука на зуммере
def bequiet():
    buzzer.duty_u16(0)  # Отключаем зуммер (громкость = 0)

# Функция для обработки значения влажности почвы и вывода его в последовательный порт
def Print(x):
    # Выводим информацию в последовательный порт
    uart.write('Moisture level: {}\n'.format(x))
    
    if x > 20000:                        # Почва слишком сухая
        playtone(330)                    # Включаем звуковой сигнал с частотой 330 Гц
        Led_R.duty_u16(65535)            # Включаем красный светодиод
        Led_G.duty_u16(0)                # Выключаем зеленый светодиод
        Led_B.duty_u16(0)                # Выключаем синий светодиод
        print('Moisture level: {}\n'.format(x))
       
    elif 15000 < x and x < 20000:        # Нормальная влажность почвы
        bequiet()                        # Выключаем зуммер
        Led_R.duty_u16(0)                # Выключаем красный светодиод
        Led_G.duty_u16(65535)            # Включаем зеленый светодиод
        Led_B.duty_u16(0)                # Выключаем синий светодиод
        print('Moisture level: {}\n'.format(x))
# Основной цикл программы
def loop():
    while True:
        Moist = Moisture.read_u16()      # Считываем значение влажности почвы
        Print(Moist)                     # Вызываем функцию для обработки уровня влажности
        sleep(0.2)                       # Задержка в 200 миллисекунд перед следующим измерением

# Главная точка входа
if __name__ == '__main__':
    setup()  # Настройка датчиков
    loop()   # Запуск основного цикла
