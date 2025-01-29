# Video https://youtu.be/FrG2clX1L6U
# Post http://kontakts.ru/showthread.php/40884?p=86128#post86128
from machine import Pin, PWM, ADC
from utime import sleep

# Инициализация пина PIR (датчик движения) как входного с подтягивающим резистором
PIR = Pin(0, Pin.IN, Pin.PULL_DOWN)

# Инициализация пинов для RGB-светодиодов
Led_R = PWM(Pin(2))  # Красный светодиод
Led_G = PWM(Pin(3))  # Зеленый светодиод
Led_B = PWM(Pin(4))  # Синий светодиод

# Установка частоты ШИМ для всех светодиодов
Led_R.freq(2000)   
Led_G.freq(2000)   
Led_B.freq(2000)

# Инициализация пина для фоторезистора (GP26)
photoresistor = ADC(Pin(26))  # Считывание с аналогового пина GP26

# Переменная для отслеживания предыдущего состояния PIR
previous_state = PIR.value()

# Функция для определения времени суток
def get_time_of_day(light_level):
    if light_level > 50000:  # Ночь (очень темно)
        return "Ночь"
    elif light_level > 30000:  # Вечер
        return "Вечер"
    elif light_level > 10000:  # Утро
        return "Утро"
    else:  # День (очень светло)
        return "День"

# Функция для управления состоянием системы охраны
def control_security_system(time_of_day):
    if time_of_day == "Ночь":
        return True  # Включаем систему охраны ночью
    else:
        return False  # Выключаем систему охраны днем и вечером

if __name__ == '__main__':
    while True:
        # Считываем значение с фоторезистора (0-65535)
        light_level = photoresistor.read_u16()  # Считывание уровня освещенности

        # Определяем время суток на основе освещенности
        time_of_day = get_time_of_day(light_level)

        # Выводим значение сопротивления (уровень освещенности) и время суток
        print(f"Значение сопротивления (уровень освещенности): {light_level}, Время суток: {time_of_day}")

        # Управление системой охраны
        security_system_enabled = control_security_system(time_of_day)
        if security_system_enabled:
            print("Система охраны включена")
        else:
            print("Система охраны выключена")

        # Если система охраны включена и обнаружено движение
        if security_system_enabled:
            # Проверяем состояние PIR и выводим информацию, если оно изменилось
            current_state = PIR.value()
            if current_state != previous_state:
                if current_state == 1:  # Движение обнаружено
                    print("Датчик движения: Движение")
                    Led_R.duty_u16(65535)  # Включаем светодиоды (белый свет)
                    Led_G.duty_u16(65535)
                    Led_B.duty_u16(65535)
                    sleep(3)  # Пауза 3 секунды
                else:  # Нет движения
                    print("Датчик движения: Без движения")
                    Led_R.duty_u16(0)  # Выключаем светодиоды
                    Led_G.duty_u16(0)
                    Led_B.duty_u16(0)
                previous_state = current_state  # Обновляем состояние
        else:
            # Если система охраны выключена, выключаем светодиоды
            Led_R.duty_u16(0)
            Led_G.duty_u16(0)
            Led_B.duty_u16(0)

        sleep(1)  # Пауза 1 секунда перед следующим циклом
