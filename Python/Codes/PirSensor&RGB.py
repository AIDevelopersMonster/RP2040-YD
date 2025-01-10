# Video
# Post
from machine import Pin, PWM
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

# Переменная для отслеживания предыдущего состояния
previous_state = PIR.value()

if __name__ == '__main__':
    while True:
        # Получаем текущее состояние пина PIR
        current_state = PIR.value()
        
        # Если текущее состояние отличается от предыдущего, выводим и обновляем состояние
        if current_state != previous_state:
            print(f"Датчик движения: {'Движение' if current_state == 1 else 'Без движения'}")
            previous_state = current_state  # Обновляем состояние

            # Управление светодиодами в зависимости от состояния
            if current_state == 1:  # Движение
                Led_R.duty_u16(65535)  # Включаем светодиоды на максимальную яркость (белый цвет)
                Led_G.duty_u16(65535)
                Led_B.duty_u16(65535)
                sleep(3)  # Пауза на 3 секунды
            else:  # Без движения
                Led_R.duty_u16(0)  # Выключаем светодиоды
                Led_G.duty_u16(0)
                Led_B.duty_u16(0)
