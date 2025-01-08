import machine
import time

# Массив пинов GPIO (исключаем зарезервированные пины)
gpio_pins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 26, 27, 28]

# Создаем пины как выходы
pins = [machine.Pin(pin, machine.Pin.OUT) for pin in gpio_pins]

while True:
    # Включаем все пины
    for pin in pins:
        pin.on()
    
    # Задержка 0,5 секунды
    time.sleep(0.5)

    # Выключаем все пины
    for pin in pins:
        pin.off()

    # Задержка 0,5 секунды
    time.sleep(0.5)
