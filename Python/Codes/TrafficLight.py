# Video https://youtu.be/TbPmAjyyn54
# Post http://kontakts.ru/showthread.php/40884?p=86154#post86154
from machine import Pin, I2C
import time
import tm1637

# Инициализация 7-сегментного дисплея
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(3))

# Инициализация пинов для управления светодиодами (красный, желтый, зеленый)
Led_R = Pin(6, Pin.OUT)
Led_Y = Pin(7, Pin.OUT)
Led_G = Pin(8, Pin.OUT)

# Инициализация пассивного зуммера на пине 9
buzzer = Pin(9, Pin.OUT)

# Инициализация кнопки на пине 10
button = Pin(10, Pin.IN, Pin.PULL_UP)

# Инициализация I2C для DS3231
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
address = 0x68  # Адрес DS3231

# Переменная для режима
mode = 1

# Время последнего нажатия кнопки
last_button_press = 0

# Минимальное время между нажатием кнопки (в миллисекундах)
debounce_delay = 300

def buzz(frequency, duration):
    """Генерация звукового сигнала на пассивном зуммере."""
    period = 1 / frequency
    for _ in range(duration):
        buzzer.value(1)
        time.sleep(period / 2)
        buzzer.value(0)
        time.sleep(period / 2)

def switch_mode(pin):
    """Переключение между режимами с учетом дебаунса."""
    global mode, last_button_press
    current_time = time.ticks_ms()  # Время в миллисекундах
    if time.ticks_diff(current_time, last_button_press) > debounce_delay:  # Если прошло достаточно времени с последнего нажатия
        mode = 1 if mode == 2 else 2
        print("Switching to mode", mode)
        last_button_press = current_time  # Обновляем время последнего нажатия

def read_time():
    """Чтение времени с DS3231 и преобразование формата BCD в десятичный."""
    data = i2c.readfrom_mem(address, 0x00, 7)  # Чтение 7 байтов данных
    second = bcd_to_dec(data[0] & 0x7F)  # Преобразуем BCD в десятичный формат
    minute = bcd_to_dec(data[1] & 0x7F)
    hour = bcd_to_dec(data[2] & 0x3F)
    day = bcd_to_dec(data[4] & 0x3F)
    month = bcd_to_dec(data[5] & 0x1F)
    year = bcd_to_dec(data[6]) + 2000  # Год в формате 20xx
    
    return year, month, day, hour, minute, second

def bcd_to_dec(bcd):
    """Преобразование значения BCD в десятичное."""
    return (bcd >> 4) * 10 + (bcd & 0x0F)

# Настройка прерывания для кнопки с дебаунсом
button.irq(trigger=Pin.IRQ_FALLING, handler=switch_mode)

if __name__ == '__main__':
    while True:
        print(f"Current mode: {mode}")
        
        if mode == 1:  # Режим 1
        
            num = 30
            Led_R.value(1)
            print("Red light ON")
            for i in range(30):
                num = num - 1
                tm.number(num)
                time.sleep(1)
            Led_R.value(0)
            print("Red light OFF")
            for i in range(5):
                Led_Y.value(1)
                time.sleep(0.3)
                Led_Y.value(0)
                time.sleep(0.3)

            Led_G.value(1)
            print("Green light ON")
            num = 10
            while num >= 0:
                tm.number(num)
                buzz(frequency=1000, duration=10)
                time.sleep(1)
                num -= 1
            Led_G.value(0)
            print("Green light OFF")

        elif mode == 2:  # Режим 2 (мигание желтым и отображение времени)
            print("Mode 2: Flashing yellow and showing time")
            for i in range(10):
                Led_Y.value(1)
                time.sleep(0.5)
                Led_Y.value(0)
                time.sleep(0.5)

                # Чтение времени с DS3231
                year, month, day, hour, minute, second = read_time()
                time_str = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
                tm.number(int(time_str.replace(":", "")[:4]))  # Отображаем только первые 4 цифры (часы и минуты)

