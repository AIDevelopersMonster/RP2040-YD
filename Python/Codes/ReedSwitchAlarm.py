# Video https://youtu.be/XESUxDL97mc
# Post http://kontakts.ru/showthread.php/40884?p=86135#post86135
import utime
from machine import Pin, PWM

# Пины для подключения RGB светодиодов и кнопки
Led_R = PWM(Pin(2))    # Красный светодиод
Led_G = PWM(Pin(3))    # Зелёный светодиод
Led_B = PWM(Pin(4))    # Синий светодиод
buzzer = PWM(Pin(12))  # Базер (зуммер)
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Кнопка для сброса сигнализации
reed_switch_sensor = Pin(13, Pin.IN, Pin.PULL_UP)  # Датчик вибрации

# Частоты для PWM
Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)
buzzer.freq(1000)  # Частота для базера

# Переменные для контроля состояния сигнализации
alarm_triggered = False  # Индикатор состояния сигнализации

# Функция для сброса сигнализации
def reset_alarm(pin):
    global alarm_triggered
    alarm_triggered = False
    Led_R.duty_u16(0)
    Led_G.duty_u16(0)
    Led_B.duty_u16(0)
    buzzer.duty_u16(0)
    print("Alarm reset")

# Настроим прерывание для кнопки
button.irq(trigger=Pin.IRQ_FALLING, handler=reset_alarm)

# Основной цикл программы
while True:
    if reed_switch_sensor.value() == 0:  # Если датчик вибрации замкнул контакты
        alarm_triggered = True
        print("Open detected, alarm triggered!")

    if alarm_triggered:
        # Полицейская мигалка
        # Включаем сирену с низкой частотой
        buzzer.freq(750)
        buzzer.duty_u16(30000)  # Задаем громкость

        Led_R.duty_u16(65535)  # Красный
        Led_G.duty_u16(0)  # Зеленый
        Led_B.duty_u16(0)  # Синий
        utime.sleep_ms(300)

        # Включаем сирену с высокой частотой
        buzzer.freq(1500)
        Led_R.duty_u16(0)  # Красный
        Led_G.duty_u16(0)  # Зеленый
        Led_B.duty_u16(65535)  # Синий
        utime.sleep_ms(300)
        
    else:
        # Выключаем все при отсутствии сигнала тревоги
        Led_R.duty_u16(0)
        Led_G.duty_u16(0)
        Led_B.duty_u16(0)
        buzzer.duty_u16(0)  # Выключаем базер
    
    utime.sleep(0.1)
# Напишите здесь свой код :-)
