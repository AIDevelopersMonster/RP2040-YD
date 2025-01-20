# Video https://youtu.be/nvgrd8tqUyM?si=KbAXPRwdpcTkV6ua
# Post http://kontakts.ru/showthread.php/40884?p=86159#post86159
from machine import Pin, ADC, PWM, I2C
from i2c_lcd import I2cLcd    
from time import sleep

DEFAULT_I2C_ADDR = 0x27     # LCD 1602 I2C address
Fire_Sensor = ADC(26)       # Пин для инфракрасного датчика огня (аналоговый вход GP26)
Buzzer = 12                 # Пин для пассивного зуммера
led_red = Pin(4, Pin.OUT)   # Красный светодиод для тревоги
led_green = Pin(5, Pin.OUT) # Зеленый светодиод для нормального состояния
buzzer = PWM(Pin(Buzzer))   # Инициализация зуммера с использованием PWM

# Инициализация I2C и LCD
def setup():
    global lcd 
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

# Основной цикл
def loop():
    while True:
        fire_level = Fire_Sensor.read_u16()   # Считываем данные с инфракрасного датчика огня
        
        # Выводим значение с АЦП на монитор
        print("Fire Sensor Value: ", fire_level)
        
        # Пороговое значение для срабатывания тревоги (регулируйте в зависимости от датчика)
        if fire_level < 10000:                # Значение, при котором включается тревога (регулируйте по датчику)
            # Выводим предупреждение на LCD
            lcd.move_to(0, 0)
            lcd.putstr("Fire Detected!")
            
            # Красный светодиод мигает
            led_red.value(1)
            led_green.value(0)
            
            # Зуммер включается
            buzzer.duty_u16(1000)            # Устанавливаем громкость зуммера
            buzzer.freq(1000)                # Устанавливаем частоту зуммера
            sleep(0.5)
            buzzer.duty_u16(0)              # Останавливаем зуммер
            sleep(0.5)
        else:
            # В случае отсутствия тревоги
            lcd.move_to(0, 0)
            lcd.putstr("No Fire Detected")
            
            # Зеленый светодиод включается
            led_red.value(0)
            led_green.value(1)
            
            # Зуммер выключается
            buzzer.duty_u16(0)

        sleep(1)   # Задержка 1 секунда перед следующей проверкой
        lcd.clear() # Очистка экрана перед следующей итерацией

# Основная часть программы
if __name__ == '__main__':
    setup()  # Настройка LCD и сенсора
    loop()   # Запуск основного цикла
