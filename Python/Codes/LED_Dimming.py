# Video https://youtu.be/-bJ9fehkRLo
# Post http://kontakts.ru/showthread.php/40884?p=86140#post86140
from machine import Pin, ADC, PWM
from time import sleep

# Пин для подключения светодиода (PWM)
Led_pin = 15

# Пин для подключения потенциометра (ADC0 на GP26)
Potentiometer_pin = 0  # ADC0 multiplexing pin is GP26

def setup():
    global LED
    global Pot_ADC

    # Настройка ШИМ (PWM) для управления яркостью светодиода
    LED = PWM(Pin(Led_pin))
    LED.freq(2000)  # Устанавливаем частоту работы светодиода на 2 кГц

    # Настройка АЦП для чтения значения с потенциометра
    Pot_ADC = ADC(Potentiometer_pin)

def loop():
    while True:
        # Чтение значения с потенциометра и вывод его в консоль
        print('Potentiometer Value:', Pot_ADC.read_u16())
        
        # Считывание значения с потенциометра
        Value = Pot_ADC.read_u16()

        # Если значение с потенциометра меньше 350, устанавливаем PWM уровень 0 (выключаем светодиод)
        if Value < 450:
            LED.duty_u16(0)  # Установить яркость светодиода на 0
        else:
            # Управление яркостью светодиода в зависимости от значения потенциометра
            LED.duty_u16(Value)

        # Задержка 0.2 секунды, чтобы избежать чрезмерной частоты обновлений
        sleep(0.2)

if __name__ == '__main__':
    setup()  # Инициализация всех настроек
    loop()   # Запуск основного цикла
